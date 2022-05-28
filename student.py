from cProfile import label
from cgitb import text
from email.mime import image
from textwrap import fill
from tkinter import*
from tkinter import ttk
from tkinter.tix import Select
from turtle import update, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()

        # First Image
        img1 = Image.open(r"F:\face recognition\Images\img12.jpg")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lb1 = Label(self.root, image=self.photoimg1)
        f_lb1.place(x=0, y=0, width=500, height=130)

        # second Image
        img2 = Image.open(r"F:\face recognition\Images\img13.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lb2 = Label(self.root, image=self.photoimg2)
        f_lb2.place(x=500, y=0, width=500, height=130)

        # Third Image
        img3 = Image.open(r"F:\face recognition\Images\img14.png")
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lb3 = Label(self.root, image=self.photoimg3)
        f_lb3.place(x=1000, y=0, width=550, height=130)

        # bg image
        img4 = Image.open(r"F:\face recognition\Images\img10.jpg")
        img4 = img4.resize((1530, 660), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=660)

        title_lb1 = Label(bg_img, text="STUDENT  MANAGEMENT  SYSTEM", font=(
            "time new roman", 35, "bold"), bg="white", fg="red")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1480, height=580)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("time new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=560)

        img_left = Image.open(r"F:\face recognition\Images\img15.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lb3 = Label(Left_frame, image=self.photoimg_left)
        f_lb3.place(x=5, y=0, width=720, height=130)

        # Current course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("time new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=115)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=(
            "time new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "time new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department",
                               "Computer Science", "IT", "Mechanical", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=(
            "time new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "time new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "CSE", "CSAI", "MAE", "CE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=(
            "time new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "time new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2020-21",
                                "2021-22", "2022-23", "2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=(
            "time new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "time new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "1", "2", "3", "4")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("time new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=280)

        # Student_ID
        studentId_label = Label(class_student_frame, text="Student_ID", font=(
            "time new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentId_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_std_id, width=20, font=("time new roman", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name", font=(
            "time new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_std_name, width=20, font=("time new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_student_frame, text="Class Division", font=(
            "time new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_div, width=20, font=("time new roman", 13, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_student_frame, text="Enroll No", font=(
            "time new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=20, font=(
            "time new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender", font=(
            "time new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, width=20, font=(
            "time new roman", 13, "bold"))
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_student_frame, text="DOB", font=(
            "time new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=(
            "time new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email", font=(
            "time new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "time new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_label = Label(class_student_frame, text="Phone_No", font=(
            "time new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=(
            "time new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # radio buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

    
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn1.grid(row=6, column=1)

        # button frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=180, width=715, height=30)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", width=17,command=self.update_data, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", width=17,command=self.delete_data, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", width=17,command=self.reset_data, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=210, width=715, height=30)

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", width=35,command=self.generate_dataset, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("time new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=560)

        img_right = Image.open(r"F:\face recognition\Images\img15.jpg")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lb3 = Label(Right_frame, image=self.photoimg_right)
        f_lb3.place(x=5, y=0, width=720, height=130)

        # Searching System
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("time new roman", 12, "bold"))
        search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(search_frame, text="Search", font=(
            "time new roman", 13, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=(
            "time new roman", 13, "bold"), state="readonly", width=20)
        search_combo["values"] = ("Select", "Enroll_No", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            search_frame, width=13, font=("time new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        show_btn = Button(search_frame, text="Display", width=12, font=(
            "time new roman", 13, "bold"), bg="blue", fg="white")
        show_btn.grid(row=0, column=4, padx=4)

        # Table Frame
        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=320)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            "Dep", "Course", "Year", "Sem", "ID", "Name", "Div.", "Enroll_No", "Gender", "DOB", "Email", "Phone", "Photo"))

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("ID", text="Student_ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Div.", text="Division")
        self.student_table.heading("Enroll_No", text="Enroll_No")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Photo", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Div.", width=100)
        self.student_table.column("Enroll_No", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # function declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Please Fill the details.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Archana@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_radio1.get()

                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # Fetch Data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Archana@123", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_radio1.set(data[12])

    #update Fn
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please Fill the details.", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update?",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Archana@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Enroll_No=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Photo=%s where Student_id=%s",(
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_std_id.get()

                                                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #Delete Fn
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Archana@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset fn
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")

    #Generate dataset by taking photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please Fill the details.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Archana@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Enroll_No=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Photo=%s where Student_id=%s",(
                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_std_id.get()==id+1

                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predine data on face frontal from opencv

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





        








if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
