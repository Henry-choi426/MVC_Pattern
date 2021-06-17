import cx_Oracle
from dto import EmpDTO

class EmpDAO:
    def empdelete(self,empno): # 데이터 삭제 delete
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe") # 접속
            try:
                cur = conn.cursor()
                cur.execute("delete from emp01 where empno=:empno", empno=empno) # deptno 값 대입하여 delete
                conn.commit() # 저장
            except Exception as e:
                print(e)
            finally:
                cur.close()
                conn.close()
        except Exception as e:
            print(e)

    def empupdate(self,dto1):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe") # 접속
            try:
                cur = conn.cursor()
                cur.execute("update emp01 set sal=:sal where empno = :empno",\
                            empno = dto1.getEmpno(), sal = dto1.getSal())
                conn.commit() # 저장
            except Exception as e:  # 에러가 날 경우 print 'e'
                print(e) 
            finally:
                cur.close() # 자원 반환
                conn.close()
        except Exception as e:
            print(e)

    def empinsert(self, dto1): # empDTO 객체를 통으로 매게변수 값으로 받을 예정

        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute( "insert into emp01 values (:empno, :ename, :sal)",\
                            empno = dto1.getEmpno(), ename = dto1.getEname(), sal = dto1.getSal())
                print("---------------")
                conn.commit()
                # data = '{"ename":"' + row[1] + '", "sal":' + str(row[2]) +'}'
            except Exception as e: # 예외..
                print(e) # print e
        except Exception as e:
            print(e) # print e
        finally:
            cur.close() # 자원 반환
            conn.close()

        # return data

    # 한명의 직원정보 반환
    def empone(self, empno):
        data = ""
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from emp01 where empno=:v", v=empno) 
                row = cur.fetchone()  # set 타입으로 반환 따라서 고유한 index로 각 요소들 활용 가능
                data = '{"ename":"' + row[1] + '", "sal":' + str(row[2]) +'}'
            except Exception as e: # 예외..
                print(e) # print e
        finally:
            cur.close() # 자원 반환
            conn.close()

        return data

# if __name__ == "__main__":
    # dao = EmpDAO()
    # dto = EmpDTO(2, 'test', 100)
    # dao.empinsert(dto)

# #     print(dao.empone(7369))


'''
dao.py의 모든 코드들은  app.py에서 호출해서 사용
단 구현시에 제대로 구현하는지 구현 로직별로 확인
단위 test 지칭

방법 : 파일단위(모듈)별로 실행 가능하게 if __name__ == "__main__": 
py 파일 독립적으로 실행 가능하게 해주는 독립실행 코드
>python dao.py 
'''