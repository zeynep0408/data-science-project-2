import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = '3453'


def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn


def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('select * from pj.students where age>22 ;')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data 


def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""select * from pj.courses where category='Veritabanı'""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""select * from pj.students where first_name like 'A%' """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""select * from pj.courses where course_name ilike '%SQL%'""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('select * from pj.students where age between 22 and 24')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('select s.first_name, c.course_name  from pj.students as s inner join  pj.enrollments as e on s.student_id=e.student_id inner join pj.courses as c on e.course_id=c.course_id')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""select c.course_name ,count(e.student_id) as ogrenci_sayisi from pj.courses as c
    join pj.enrollments as e on 
     c.course_id=e.course_id
     where c.course_name ilike '%SQL%'
     group by c.course_name""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('select c.course_name,i.name as instructor_name from pj.courses as c left join pj.course_instructors as ci on c.course_id=ci.course_id left join pj.instructors as i on ci.instructor_id=i.instructor_id')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('select s.first_name from pj.students as s left join pj.enrollments as e on s.student_id=e.student_id where enrollment_date is null')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""select c.course_name , avg(age) from pj.students as s
                        join pj.enrollments as e on
                        s.student_id=e.student_id
                        join pj.courses as c on
                        e.course_id=c.course_id
                        group by c.course_name""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_11_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('select s.first_name,s.last_name ,count(c.course_id) as kurs_sayısı from pj.students as s join pj.enrollments as e on s.student_id=e.student_id join pj.courses as c on c.course_id=e.course_id group by s.first_name,last_name')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_12_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('select i.name ,count(*) from pj.instructors as i join pj.course_instructors as c on i.instructor_id=c.instructor_id group by i.name having count(*)>1')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_13_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('select c.course_name , count(distinct e.student_id) from pj.courses as c join pj.enrollments as e on c.course_id=e.course_id group by c.course_name ')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_14_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""SELECT s.first_name, s.last_name FROM pj.students AS s JOIN pj.enrollments AS e ON s.student_id = e.student_id JOIN pj.courses AS c ON e.course_id = c.course_id where c.course_name IN ('SQL Temelleri', 'İleri SQL')
 GROUP BY s.student_id, s.first_name, s.last_name
 HAVING COUNT(DISTINCT c.course_name) = 2 """)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


def question_15_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""select  s.first_name,s.last_name,i.name as instructor ,c.course_name,e.enrollment_date 
                        from pj.students as s 
                        join pj.enrollments as e on 
                        s.student_id=e.student_id 
                        join pj.courses as c on
                        e.course_id=c.course_id 
                        join pj.course_instructors as ci on 
                        e.course_id=ci.course_id
                        join pj.instructors as i on
                        ci.instructor_id=i.instructor_id""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data   