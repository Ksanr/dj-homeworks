import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    # фикстура API клиента
    return APIClient()

@pytest.fixture
def course_factory():
    # фикстура фабрика курсов
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    # фикстура фабрика студентов
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture(autouse=True)
def settings_fixture(settings):
    # Установка значения максимума студентов для тестов
    settings.MAX_STUDENT_PER_COURSER = 20



@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    # 1 проверка получения первого курса
    course = course_factory(_quantity=1)

    # response = client.get(path='/api/v1/courses/')
    response = client.get(path=f'/api/v1/courses/{course[0].id}/')
    response_data = response.json()

    assert response.status_code == 200
    assert response_data['name'] == course[0].name


@pytest.mark.django_db
def test_get_some_courses(client, course_factory):
    # 2 проверка получения списка курсов
    courses = course_factory(_quantity=10)


    response = client.get(path='/api/v1/courses/')
    response_data = response.json()

    assert len(response_data) == len(courses)
    for i, c in enumerate(response_data):
        assert response_data[i]['name'] == courses[i].name

@pytest.mark.django_db
def test_get_course_by_id(client, course_factory):
    # 3 проверка фильтрации списка курсов по id
    import random
    courses = course_factory(_quantity=10)
    select_course = random.choice(courses)
    select_id = select_course.id
    data = {'id': select_id}

    # response = client.get(path='/api/v1/courses/?id='+str(select_id))
    response = client.get(path='/api/v1/courses/', data=data)

    response_data = response.json()
    assert response_data[0]['id'] == select_id
    assert response_data[0]['name'] == select_course.name


@pytest.mark.django_db
def test_get_course_by_name(client, course_factory):
    # 4 проверка фильтрации списка курсов по name
    import random
    courses = course_factory(_quantity=10)
    select_course = random.choice(courses)
    select_name = select_course.name
    data = {'name': select_name}

    # response = client.get(path='/api/v1/courses/?name='+str(select_name))
    response = client.get(path='/api/v1/courses/', data=data)
    response_data = response.json()
    for course in response_data:
        assert course['name'] == select_name


@pytest.mark.django_db
def test_create_course(client):
    # 5 тест успешного создания курсов
    count = Course.objects.count()
    data = {'name': 'Fullstack-разработчик на Python'}

    response = client.post(path='/api/v1/courses/', data=data)
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    # 6 тест успешного обновления курсов
    import random
    courses = course_factory(_quantity=10)
    select_course = random.choice(courses)
    select_id = select_course.id
    data = {'name': 'Fullstack-разработчик на Python'}

    response = client.patch(path=f'/api/v1/courses/{select_id}/', data=data)
    assert response.status_code == 200

    # response = client.get(path=f'/api/v1/courses/{select_id}/')
    response_data = response.json()
    assert response_data['name'] == data['name']

@pytest.mark.django_db
def test_delete_course(client, course_factory):
    # 7 тест успешного удаления курса
    import random
    courses = course_factory(_quantity=10)
    select_course = random.choice(courses)
    select_id = select_course.id
    count = Course.objects.count()

    response = client.delete(path=f'/api/v1/courses/{select_id}/')
    assert response.status_code == 204
    assert Course.objects.count() == count - 1

@pytest.mark.django_db
@pytest.mark.parametrize(
    'students_count,status',
    [
        (19, True), # Для успешного исхода
        (20, False), # Превышение лимита
    ]
)
def test_add_students(students_count, status):
    # 8, 9 Тест по ограничению числа студентов
    course = Course.objects.create(name='Test Course')
    students = []
    for i in range(students_count + 1):
        student = Student.objects.create(name=f'student{i}')
        students.append(student)


    try:
        for student in students[:students_count]:
            course.add_student(student)

        result = course.add_student(students[-1])
        assert status is True
    except ValueError as e:
        assert str(e) == 'Достигнут максимальный предел студентов на курсе'
        assert status is False


def test_with_specific_settings(settings):
    # 10 тест на ограничения по примеру
    settings.MAX_STUDENT_PER_COURSER = True
    assert settings.MAX_STUDENT_PER_COURSER