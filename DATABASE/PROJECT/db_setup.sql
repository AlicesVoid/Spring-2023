CREATE TABLE address (
  address_id INT NOT NULL AUTO_INCREMENT,
  street VARCHAR(255),
  city VARCHAR(255),
  state CHAR(2),
  zip_code INT,
  PRIMARY KEY (address_id)
);

CREATE TABLE phone_num (
  phone_id BIGINT NOT NULL AUTO_INCREMENT,
  area_code INT,
  seven_digit_num BIGINT,
  PRIMARY KEY (phone_id)
);

CREATE TABLE professor (
  ssn BIGINT NOT NULL,
  Paddress_id INT NOT NULL,
  Pphone_id BIGINT NOT NULL UNIQUE,
  Pname VARCHAR(60),
  sex CHAR(1) CHECK (sex IN ('M', 'F', 'X')),
  title VARCHAR(30),
  salary INT,
  degrees VARCHAR(255),
  PRIMARY KEY (ssn),
  FOREIGN KEY (Paddress_id) REFERENCES address(address_id),
  FOREIGN KEY (Pphone_id) REFERENCES phone_num(phone_id)
);

CREATE TABLE department (
  dnum INT NOT NULL,
  chair_id BIGINT NOT NULL,
  Dphone_id BIGINT NOT NULL UNIQUE,
  Dname VARCHAR(30),
  Dlocation VARCHAR(10),
  PRIMARY KEY (dnum),
  FOREIGN KEY (chair_id) REFERENCES professor(ssn),
  FOREIGN KEY (Dphone_id) REFERENCES phone_num(phone_id)
);

CREATE TABLE course (
  cnum INT NOT NULL,
  dept_id INT NOT NULL,
  units TINYINT,
  textbook VARCHAR(255),
  PRIMARY KEY (cnum, dept_id),
  FOREIGN KEY (dept_id) REFERENCES department(dnum)
);

CREATE TABLE prerequisites (
  course_cnum INT NOT NULL,
  course_dept_id INT NOT NULL,
  prerequisite_cnum INT NOT NULL,
  prerequisite_dept_id INT NOT NULL,
  PRIMARY KEY (course_cnum, course_dept_id, prerequisite_cnum, prerequisite_dept_id),
  FOREIGN KEY (course_cnum, course_dept_id) REFERENCES course(cnum, dept_id),
  FOREIGN KEY (prerequisite_cnum, prerequisite_dept_id) REFERENCES course(cnum, dept_id)
);

CREATE TABLE course_section (
  snum TINYINT NOT NULL,
  course_id INT NOT NULL,
  sdept_id INT NOT NULL,
  seats TINYINT,
  meeting_days VARCHAR(21),
  start_time TIME,
  ending_time TIME,
  classroom VARCHAR(10),
  PRIMARY KEY (snum, course_id, sdept_id),
  FOREIGN KEY (course_id, sdept_id) REFERENCES course(cnum, dept_id)
);

CREATE TABLE minor (
  min_cwid BIGINT NOT NULL,
  min_dnum INT NOT NULL,
  PRIMARY KEY (min_cwid, min_dnum),
  FOREIGN KEY (min_cwid) REFERENCES student(cwid),
  FOREIGN KEY (min_dnum) REFERENCES department(dnum)
);

CREATE TABLE student (
  cwid BIGINT NOT NULL,
  Saddress_id INT NOT NULL,
  Sphone_id BIGINT NOT NULL,
  major_id INT NOT NULL,
  fname VARCHAR(30),
  lname VARCHAR(30),
  PRIMARY KEY (cwid),
  FOREIGN KEY (Saddress_id) REFERENCES address(address_id),
  FOREIGN KEY (Sphone_id) REFERENCES phone_num(phone_id),
  FOREIGN KEY (major_id) REFERENCES department(dnum)
);

CREATE TABLE enroll_record (
  er_cwid BIGINT NOT NULL,
  er_snum TINYINT NOT NULL,
  er_cnum INT NOT NULL,
  er_dnum INT NOT NULL,
  grade VARCHAR(2),
  PRIMARY KEY (er_cwid, er_snum, er_cnum, er_dnum),
  FOREIGN KEY (er_cwid) REFERENCES student(cwid),
  FOREIGN KEY (er_snum, er_cnum, er_dnum) REFERENCES course_section(snum, course_id, sdept_id),
  CHECK (grade IN ('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'IP', 'CR', 'NC', 'W', 'WM', 'WD'))
);

