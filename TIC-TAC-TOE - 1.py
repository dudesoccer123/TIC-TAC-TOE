# import libraries 

from tkinter import *
from tkinter import messagebox # to show message prompts as and when required
from tkinter.font import Font
import mysql.connector # create a connection with the mysql database.

mc = mysql.connector.connect(host = 'localhost',user = 'root',database = 'pcps',password = '<your database host password>')
cursor = mc.cursor()

def crtable():
    cursor.execute('''select count(*) from information_schema.tables
    where table_schema = 'pcps';''')
    data1 = cursor.fetchall()
    if data1 != [(2,)]:
        cursor.execute("create table userdetails (username char(30) primary key,password varchar(10),wins int,losses int,draws int, points int);")

#crtable()  # function to create a table in the database. 


# Update usernames List
b=[]
cursor.execute('select username from userdetails;')
d = cursor.fetchall()

for i in range (0,len(d)):
    for j in d[i]:
        b.append(j)
        
def RefreshUserList():
    cursor.execute('select username from userdetails;')
    d = cursor.fetchall()

    for i in range (0,len(d)):
        for j in d[i]:
            b.append(j)   
   
RefreshUserList()   

def chpass(uname): # obtain corresponding password for the username.

    cursor.execute("select password from userdetails where username = '%s'" %(uname))

    data = cursor.fetchall()

    v =[]
    for row in data:
        for col_value in row:
            v.append(col_value)
    return v


# define the main tkinter project 
root = Tk()
root.title("Tic-Tac-SToe")
root.geometry("700x450")
root.resizable(False,False)

# define Functions

my_font = Font(         # fonts used in the UI
    family = 'Times',
    size = 50,
    weight = 'bold',
    slant = 'italic',
    underline = False,
    overstrike = False
)

my_font_2 = Font(
    family = 'Times',
    size = 27,
    weight = 'bold',
    #slant = 'roman',
    underline = False,
    overstrike = False
)


# X starts first: 
clicked = True # when its x's turn is is False when o's turn.
count = 0 # records the number of moves 
symbol = 'x'



# functions



def b_clicked(b): # function to change the putton text to x or O based on whose turn it is 
    global clicked,count
    if b['text'] == ' ' and clicked == True:
        b['text'] = 'X'
        clicked = False 
        turn_o_frame.tkraise()
        count += 1
        check_win()
    elif b['text'] == ' ' and clicked == False:
        b['text'] = 'O'
        clicked = True
        turn_x_frame.tkraise()
        count += 1
        check_win()
    else:
        messagebox.showerror("Tic-Tac-Toe","That box has already been selected! \n please pick another box.")

def disable_btn(): # disables all buttons and no further clicks can take place
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)


def points_x(): # awarding points based on the winner
    if n1 != winner:
        cursor.execute("update userdetails set points = points+5 where username = '%s'" % (n1))
        cursor.execute("update userdetails set wins = wins+1 where username = '%s'" % (n1))
        cursor.execute("update userdetails set losses = losses+1 where username = '%s'" % (n2))
    mc.commit()
def points_o():
    if n2 != winner:
        cursor.execute("update userdetails set points = points+5 where username = '%s'" % (n2))
        cursor.execute("update userdetails set wins = wins+1 where username = '%s'" % (n2))
        cursor.execute("update userdetails set losses = losses+1 where username = '%s'" % (n1))
    mc.commit()
def check_win():  # contains all if condition row wise, column wise and diagonal wise. for win of x and o
    global winner
    winner = False

    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text']== 'X':
        b1.config(bg = '#A5F1E9')
        b2.config(bg = '#A5F1E9')
        b3.config(bg = '#A5F1E9')
        winner = True
        x_win_number()
        points_x()
        disable_btn()
        #destroy_btn()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text']== 'X':
        b4.config(bg = '#A5F1E9')
        b5.config(bg = '#A5F1E9')
        b6.config(bg = '#A5F1E9')
        winner = True
        x_win_number()
        points_x()
        disable_btn()
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text']== 'X':
        b7.config(bg = '#A5F1E9')
        b8.config(bg = '#A5F1E9')
        b9.config(bg = '#A5F1E9')
        winner = True
        x_win_number()
        points_x()
        disable_btn()
    
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text']== 'X':
        b1.config(bg = '#A5F1E9')
        b4.config(bg = '#A5F1E9')
        b7.config(bg = '#A5F1E9')
        winner = True
        x_win_number()
        points_x()
        disable_btn()
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text']== 'X':
        b2.config(bg = '#A5F1E9')
        b5.config(bg = '#A5F1E9')
        b8.config(bg = '#A5F1E9')
        winner = True
        x_win_number()
        points_x()
        disable_btn()
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text']== 'X':
        b3.config(bg = '#A5F1E9')
        b6.config(bg = '#A5F1E9')
        b9.config(bg = '#A5F1E9')
        winner = True
        x_win_number()
        points_x()
        disable_btn()
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text']== 'X':
        b1.config(bg = '#A5F1E9')
        b5.config(bg = '#A5F1E9')
        b9.config(bg = '#A5F1E9')
        winner = True
        x_win_number()
        points_x()
        disable_btn()
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text']== 'X':
        b3.config(bg = '#A5F1E9')
        b5.config(bg = '#A5F1E9')
        b7.config(bg = '#A5F1E9')
        winner = True
        x_win_number()
        points_x()
        disable_btn()

    # check a tie :
    if count == 9 and winner == False : 
        tie_number()
        cursor.execute("update userdetails set points = points+2 where username = '%s'" % (n1))
        mc.commit()
        cursor.execute("update userdetails set draws = draws+1 where username = '%s'"%(n1))
        mc.commit()
        cursor.execute("update userdetails set draws = draws+1 where username = '%s'"%(n2))
        mc.commit()
        cursor.execute("update userdetails set points = points+2 where username = '%s'" % (n2))
        mc.commit()
        disable_btn()

    ################# check for o win

    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text']== 'O':
        b1.config(bg = '#A5F1E9')
        b2.config(bg = '#A5F1E9')
        b3.config(bg = '#A5F1E9')
        winner = True
        o_win_number()
        points_o()
        disable_btn()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text']== 'O':
        b4.config(bg = '#A5F1E9')
        b5.config(bg = '#A5F1E9')
        b6.config(bg = '#A5F1E9')
        winner = True
        o_win_number()
        points_o()
        disable_btn()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text']== 'O':
        b7.config(bg = '#A5F1E9')
        b8.config(bg = '#A5F1E9')
        b9.config(bg = '#A5F1E9')
        winner = True
        o_win_number()
        points_o()
        disable_btn()
    
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text']== 'O':
        b1.config(bg = '#A5F1E9')
        b4.config(bg = '#A5F1E9')
        b7.config(bg = '#A5F1E9')
        winner = True
        o_win_number()
        points_o()
        disable_btn()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text']== 'O':
        b2.config(bg = '#A5F1E9')
        b5.config(bg = '#A5F1E9')
        b8.config(bg = '#A5F1E9')
        winner = True
        o_win_number()
        points_o()
        disable_btn()
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text']== 'O':
        b3.config(bg = '#A5F1E9')
        b6.config(bg = '#A5F1E9')
        b9.config(bg = '#A5F1E9')
        winner = True
        o_win_number()
        points_o()
        disable_btn()
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text']== 'O':
        b1.config(bg = '#A5F1E9')
        b5.config(bg = '#A5F1E9')
        b9.config(bg = '#A5F1E9')
        winner = True
        o_win_number()
        points_o()
        disable_btn()
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text']== 'O':
        b3.config(bg = '#A5F1E9')
        b5.config(bg = '#A5F1E9')
        b7.config(bg = '#A5F1E9')
        winner = True
        o_win_number()
        points_o()
        disable_btn()
    



# functions to raise respective frames ( for the transitions from 1 tab to another.)
def go_to_login(): 
    login_frame.tkraise()

def back_to_home():
    home_frame.tkraise()

def back_to_game():
    main_frame.tkraise()

def go_to_create():
    usernameentry1.delete(0, END)
    passwordentry1.delete(0, END)
    confirmpasswordentry.delete(0,END)
    Create_frame.tkraise()


def to_stats():
    stats.tkraise()

def to_edit_acc():
    accounts.tkraise()


def change_username():
    ch_username.tkraise()

def change_password():
    ch_password.tkraise()

def delete_account():
    del_acc.tkraise()

###################################################

# functions for login functionality 

def submit():         # create a new user in the database after all checks are complete.
    RefreshUserList()
    username = usernameentry1.get()
    if username not in b and username != '':
        password = passwordentry1.get()
        conpassword = confirmpasswordentry.get()
        if password == conpassword and password != '' and conpassword != '':
            add_user = ('''insert into userdetails
            values (%s, %s,0,0,0,0);''')
            data_user = (username,password)
            cursor.execute(add_user,data_user) # sql query to add the data.
            mc.commit()
            print('User created')
            messagebox.showinfo("","User successfully created")
            RefreshUserList()
            home_frame.tkraise()
            usernameentry1.delete(0,END)
            passwordentry1.delete(0,END)
            confirmpasswordentry.delete(0,END)
        elif password == '':
            print('Please enter the password')
            messagebox.showinfo("","Please enter the password")
            confirmpasswordentry.delete(0,END)
        elif conpassword == '':
            print('Please confirm the password')
            messagebox.showinfo("","Please confirm the password")
        else:
            print("Password doesnt match")
            messagebox.showinfo("","Password does not match")
            passwordentry1.delete(0,END)
            confirmpasswordentry.delete(0,END)
    elif username == '':
        print('Please enter the username')
        messagebox.showwarning("ERROR","Please enter the username")
        usernameentry1.delete(0,END)
        passwordentry1.delete(0,END)
        confirmpasswordentry.delete(0,END)
    else:
        print("Username already taken")
        messagebox.showinfo("","Selected username is already taken")
        usernameentry1.delete(0,END)
        passwordentry1.delete(0,END)
        confirmpasswordentry.delete(0,END)


def play_game():
    '''code to check if entered credentials are correct.
        if correct then raise the screen to play the game. else prompt to re-enter.
    '''
    username_1 = usernameentry_p1.get()
    username_2 = usernameentry_p2.get()
    password_1 = passwordentry_p1.get()
    password_2 = passwordentry_p2.get()
    
    global n1
    global n2
    global w1
    global w2
    global maindata
    n1 = username_1
    w1 = password_1
    n2 = username_2
    w2 = password_2
    if username_1 != username_2:
        if username_1 in b:
            v = chpass(username_1)
            print(v)
            if password_1 in v:
                maindata = []
                if username_2 in b:
                    v = chpass(username_2)
                    if password_2 in v:
                        maindata = []
                        main_frame.tkraise()

                        cursor.execute(f"select wins from userdetails where username = '%s'"%(n1))
                        w_n1 = cursor.fetchone()[0]
                        cursor.execute(f"select losses from userdetails where username = '%s'"%(n1))
                        l_n1 = cursor.fetchone()[0]
                        cursor.execute(f"select draws from userdetails where username = '%s'"%(n1))
                        d_n1 = cursor.fetchone()[0]
                        cursor.execute(f"select points from userdetails where username = '%s'"%(n1))
                        p_n1 = cursor.fetchone()[0]
                        n1_label = Label(stats,text=f'Game statistics for {n1}:',font=("Arial",20,'bold'),bg='#579BB1',fg='#ECE8DD')
                        n1_label.place(x=10,y=120)
                        n1_info = Label(stats,text=f'Wins:{w_n1} ,Losses:{l_n1}, Draws:{d_n1}, Points:{p_n1}',font=("Arial",20,'bold'),fg='#0081B4',bg='#ECE8DD')
                        n1_info.place(x=10,y=170)

                        cursor.execute(f"select wins from userdetails where username = '%s'" % (n2))
                        w_n2 = cursor.fetchone()[0]
                        cursor.execute(f"select losses from userdetails where username = '%s'" % (n2))
                        l_n2 = cursor.fetchone()[0]
                        cursor.execute(f"select draws from userdetails where username = '%s'" % (n2))
                        d_n2 = cursor.fetchone()[0]
                        cursor.execute(f"select points from userdetails where username = '%s'" % (n2))
                        p_n2 = cursor.fetchone()[0]
                        n1_label = Label(stats, text=f'Game statistics for {n2}:', font=("Arial", 20,'bold'),bg='#579BB1',fg='#ECE8DD')
                        n1_label.place(x=10, y=270)
                        n1_info = Label(stats, text=f'Wins:{w_n2}, Losses:{l_n2}, Draws:{d_n2}, Points:{p_n2}',font=("Arial", 20,'bold'),fg='#0081B4',bg='#ECE8DD')
                        n1_info.place(x=10, y=310)

                        usernameentry_p1.delete(0,END)
                        usernameentry_p2.delete(0,END)
                        passwordentry_p1.delete(0,END)
                        passwordentry_p2.delete(0,END)

                    else:
                        print("Your username or password is wrong")
                        messagebox.showwarning("ERROR","Your username or password is wrong")
                        usernameentry_p2.delete(0,END)
                        passwordentry_p2.delete(0,END)
                else:
                    print("There is no user present with the username",username_2)
                    messagebox.showwarning("ERROR","No user present with that username")
                    usernameentry_p2.delete(0,END)
                    passwordentry_p2.delete(0,END)

            else:
                print("Your username or password is wrong")
                messagebox.showwarning("ERROR","Your username or password is wrong")
                usernameentry_p1.delete(0,END)
                passwordentry_p1.delete(0,END)
        else:
            print("There is no user present with the username",username_1)
            messagebox.showwarning("ERROR","No user present with that username")
            usernameentry_p1.delete(0,END)
            passwordentry_p1.delete(0,END)
    else:
        print("cannot use same account twice.")
        messagebox.showwarning("ERROR","Cannot login with the same account twice.")
        usernameentry_p1.delete(0,END)
        passwordentry_p1.delete(0,END)
        usernameentry_p2.delete(0,END)
        passwordentry_p2.delete(0,END)

# functions for changing the account details.

def change_username_permanant():
    if old_user_enter.get() == n1 or old_user_enter.get() == n2 :
        for t in range(1):
            changeusname = new_user_enter.get()
            if changeusname in b:
                messagebox.showinfo("","Username already taken")
                RefreshUserList()
                stats.tkraise()
                break

            cursor.execute("update userdetails set username = '%s' where username = '%s'" %(changeusname,old_user_enter.get()))
            mc.commit()
            print("username changed successfully")
            messagebox.showinfo("","Username changed successfully")
            RefreshUserList()
            home_frame.tkraise()
            new_user_enter.delete(0,END)
            old_user_enter.delete(0,END)
    else:
        print("Invalid username.")
        messagebox.showwarning("ERROR","Invalid username.")
        new_user_enter.delete(0,END)
        old_user_enter.delete(0,END)


def change_password_permanant():
    ouser = old_user_2_enter.get()
    npass = new_pass_enter.get()
    if  ouser == n1 or ouser == n2:
        cursor.execute("update userdetails set password = '%s' where username = '%s'" %(npass,ouser))
        mc.commit()
        print("Password successfully changed")
        messagebox.showinfo("","Password changed successfully")
        home_frame.tkraise()
        old_user_2_enter.delete(0,END)
        new_pass_enter.delete(0,END)
    else:
        print("Try entering password again")
        messagebox.showwarning("","Entered details do not match.\n Please try again.")
        old_user_2_enter.delete(0,END)
        new_pass_enter.delete(0,END)

def delete_acc_permanant():
    if old_user_3_enter.get() == n1 or old_user_3_enter.get() == n2:
        cursor.execute("delete from userdetails where username = '%s'" %(old_user_3_enter.get()))
        mc.commit()
        print('Account successfully deleted')
        messagebox.showinfo("","Account successfully deleted")
        RefreshUserList()
        home_frame.tkraise()
        old_user_3_enter.delete(0,END)
    else:
        print("Try entering username again.")
        messagebox.showwarning("","Entered details do not match.\n Please try again.")
        old_user_3_enter.delete(0,END)


def reset():  # this function is used to start the game over by defining all the buttons again.
    turn_x_frame.tkraise()
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked = True
    count = 0
    b1 = Button(board_frame,text = " ",font = ("Arial",25),height = 2,width = 5, bg = '#6ECCAF',command= lambda: b_clicked(b1))
    b2 = Button(board_frame,text = " ",font = ("Arial",25),height = 2,width = 5, bg = '#6ECCAF',command= lambda: b_clicked(b2))
    b3 = Button(board_frame,text = " ",font = ("Arial",25),height = 2,width = 5, bg = '#6ECCAF',command= lambda: b_clicked(b3))
    b4 = Button(board_frame,text = " ",font = ("Arial",25),height = 2,width = 5, bg = '#6ECCAF',command= lambda: b_clicked(b4))
    b5 = Button(board_frame,text = " ",font = ("Arial",25),height = 2,width = 5, bg = '#6ECCAF',command= lambda: b_clicked(b5))
    b6 = Button(board_frame,text = " ",font = ("Arial",25),height = 2,width = 5, bg = '#6ECCAF',command= lambda: b_clicked(b6))
    b7 = Button(board_frame,text = " ",font = ("Arial",25),height = 2,width = 5, bg = '#6ECCAF',command= lambda: b_clicked(b7))
    b8 = Button(board_frame,text = " ",font = ("Arial",25),height = 2,width = 5, bg = '#6ECCAF',command= lambda: b_clicked(b8))
    b9 = Button(board_frame,text = " ",font = ("Arial",25),height = 2,width = 5, bg = '#6ECCAF',command= lambda: b_clicked(b9))

    b1.grid(row = 0,column = 0)
    b2.grid(row = 0,column = 1)
    b3.grid(row = 0,column = 2)
    b4.grid(row = 1,column = 0)
    b5.grid(row = 1,column = 1)
    b6.grid(row = 1,column = 2)
    b7.grid(row = 2,column = 0)
    b8.grid(row = 2,column = 1)
    b9.grid(row = 2,column = 2)

game_count=0

# functions to keep a track of the moves, wins draws etc and display it on the screen.
def game_number():
    global game_count
    game_count+=1
    label_moves = Label(main_frame, text=f'Game:{game_count}', font=('Helvetica', 20,'bold'),fg='#0081B4',bg='#ECE8DD')
    label_moves.place(x='400', y='120')

x_win=0
def x_win_number():
    global x_win
    x_win+=1
    label_x_win = Label(main_frame, text=f'No. Of X Wins : {x_win}', font=('Helvetica', 20,'bold'),fg='#0081B4',bg='#ECE8DD')
    label_x_win.place(x='400', y='270')

o_win=0
def o_win_number():
    global o_win
    o_win+=1
    label_o_win = Label(main_frame, text=f'No. Of O Wins : {o_win}', font=('Helvetica', 20,'bold'), fg='#0081B4',bg='#ECE8DD')
    label_o_win.place(x='400', y='320')

tie_no=0
def tie_number():
    global tie_no
    tie_no+=1
    label_tie_no = Label(main_frame, text=f'No. Of Ties : {tie_no}', font=('Helvetica', 20,'bold'), fg='#0081B4',bg='#ECE8DD')
    label_tie_no.place(x='400', y='370')
    

def start_game():  # this is the function that gets called when we click 'play'


    def display_moves():
        label_moves = Label(main_frame, text=f'Moves : {count}', font=('Helvetica', 20,'bold'),fg='#0081B4',bg='#ECE8DD')
        label_moves.place(x='400', y='220')
        label_moves.after(300, display_moves)

    display_moves()
    game_number()
    reset()





# frames (main part of the user interface)


# 1) Home screen 
home_frame = Frame(root,width=700,height = 450,bg='#579BB1')
home_frame.place(x=0,y=0)
decoration_1 = Frame(home_frame,width = 700,height = 100,bg = '#ECE8DD')
decoration_1.place(x=0,y=0)
t1 = Label(decoration_1,text = 'TIC-TAC-TOE',font = my_font,bg='#ECE8DD',fg='#579BB1')
t1.place(x=140,y=10)

img = PhotoImage(file='board_img.png')

namelabel = Label(home_frame,image = img)
namelabel.place(x=70,y=150)

decoration_2 = Frame(home_frame,width=250,height = 250,bg = '#ECE8DD')
decoration_2.place(x=400,y=150)
login_btn_1 = Button(decoration_2,font = ('Arial',18),text='Login', command = go_to_login,bg='#579BB1',fg='#ECE8DD')
login_btn_1.place(x=80,y=50)

new_acc_label = Label(decoration_2,font = ('Arial',15),text="Don't have an account?",fg='#0081B4',bg='#ECE8DD')
new_acc_label.place(x=20,y=120)
Create_new_acc = Button(decoration_2,font = ('Arial',18),text='Create One', command = go_to_create,bg='#579BB1',fg='#ECE8DD')
Create_new_acc.place(x=50,y=170)



# 2) login screen 

login_frame = Frame(root,width=700,height=450,bg='#ECE8DD')
login_frame.place(x=0,y=0)

player_1_label = Label(login_frame,text = "Player 1 Login 'X' :",font = ('Arial',20,'bold'),fg = '#0081B4',bg='#ECE8DD')
player_1_label.place(x = 250,y = 40)
user = Label(login_frame,text = "USERNAME :",font = ('Arial',20,'bold') ,fg = '#0081B4',bg='#ECE8DD')
user.place(x=10,y=100)
password = Label(login_frame,text = "PASSWORD :",font = ('Arial',20,'bold'),fg = '#0081B4',bg='#ECE8DD' )
password.place(x=10,y=150)
usernameentry_p1 = Entry(login_frame,font=('Arial',20),bg = '#579BB1',fg='#ECE8DD')
usernameentry_p1.place(x=200,y=100)
passwordentry_p1 = Entry(login_frame,font=('Arial',20),show='*',bg = '#579BB1',fg='#ECE8DD')
passwordentry_p1.place(x=200,y=150)

player_2_label = Label(login_frame,text = "Player 2 Login 'O' :",font = ('Arial',20,'bold'),fg = '#0081B4',bg='#ECE8DD')
player_2_label.place(x = 250,y = 250)
user2 = Label(login_frame,text = "USERNAME :",font = ('Arial',20,'bold') ,fg = '#0081B4',bg='#ECE8DD')
user2.place(x=10,y=300)
password2 = Label(login_frame,text = "PASSWORD :",font = ('Arial',20,'bold'),fg = '#0081B4',bg='#ECE8DD' )
password2.place(x=10,y=350)
usernameentry_p2 = Entry(login_frame,font=('Arial',20),bg = '#579BB1',fg='#ECE8DD')
usernameentry_p2.place(x=200,y=300)
passwordentry_p2 = Entry(login_frame,font=('Arial',20),show='*',bg = '#579BB1',fg='#ECE8DD')
passwordentry_p2.place(x=200,y=350)
login_btn = Button(login_frame,font = ('Arial',20,'bold'),text='Play >>', command = play_game,bg = '#579BB1',fg='#ECE8DD')
login_btn.place(x=550,y=370)
back_btn = Button(login_frame,font = ('Arial',15),text = 'Back',command = back_to_home,fg = '#ECE8DD',bg = '#579BB1')
back_btn.place(x=20,y = 25)


# 3) create new account
Create_frame = Frame(root,width=700,height = 450,bg = '#ECE8DD')
Create_frame.place(x=0,y=0)
decoration_3 = Frame(Create_frame,width = 700,height = 100,bg = '#579BB1')
decoration_3.place(x=0,y=0)
createacc = Label(Create_frame,text = "Create Your TIC-TAC-TOE Account",font= my_font_2,bg = '#579BB1',fg='#ECE8DD')
createacc.place(x=100,y=20)


usernamecreate = Label(Create_frame,text='ENTER USERNAME :',font=("Arial",20,'bold'),fg = '#0081B4',bg='#ECE8DD')
usernamecreate.place(x=40,y=150)
passwordcreate = Label(Create_frame,text='ENTER PASSWORD :',font=("Arial",20,'bold'),fg = '#0081B4',bg='#ECE8DD')
passwordcreate.place(x=40,y=220)
passwordconfirm = Label(Create_frame,text='CONFIRM PASSWORD :',font=("Arial",20,'bold'),fg = '#0081B4',bg='#ECE8DD')
passwordconfirm.place(x=40,y=290)
usernameentry1 = Entry(Create_frame,font=('Arial',20),bg = '#579BB1',fg='#ECE8DD')
usernameentry1.place(x=380,y=150)
passwordentry1 = Entry(Create_frame,font=('Arial',20),show='*',bg = '#579BB1',fg='#ECE8DD')
passwordentry1.place(x=380,y=220)
confirmpasswordentry = Entry(Create_frame,font=('Arial',20),show='*',bg = '#579BB1',fg='#ECE8DD')
confirmpasswordentry.place(x=380,y=290)

confirm = Button(Create_frame,text='CONFIRM',font=('Arial',20),command=submit,bg = '#579BB1',fg='#ECE8DD')
confirm.place(x=440,y=350)
textmandt = Label(Create_frame,text = "*Please fill each and every field",font=('Arial',15,'bold'),bg = '#ECE8DD',fg = '#0081B4' )
textmandt.place(x=40,y=350)
gobacktologin = Button(decoration_3,text='Back',font=("Arial",15),command = back_to_home,bg = '#ECE8DD',fg = '#0081B4')
gobacktologin.place(x=20,y=25)



# 4) game screen 

main_frame = Frame(root,width = 700, height = 450,background='#ECE8DD')
main_frame.place(x=0,y=0)
decoration_5 = Frame(main_frame,width = 700,height = 70,bg = '#579BB1')
decoration_5.place(x=0,y=0)
back_btn = Button(main_frame,text = '< back',font = ("Helvetica",15),bg = '#ECE8DD',fg = '#0081B4',command = back_to_home)
back_btn.place(x=20,y=20)
# board frame
board_frame = Frame(main_frame,background='cyan')
board_frame.place(x=20,y=120)
board_frame.tkraise()


Statistics_btn = Button(main_frame,text = 'Statistics',font = ("Helvetica",15),bg = '#ECE8DD',fg = '#0081B4',command = to_stats)
acc_settings_btn = Button(main_frame,text = 'Account Settings',font = ("Helvetica",15),bg = '#ECE8DD',fg = '#0081B4',command = to_edit_acc)

Statistics_btn.place(x=400,y=20)
acc_settings_btn.place(x=520,y=20)

# game options 
play_btn = Button(main_frame,text = 'Play',font = ("Helvetica",15),fg = '#344D67',bg = '#6ECCAF',command = start_game)
play_btn.place(x=150,y=75)


turn_o_frame = Frame(main_frame)
turn_o = Label(turn_o_frame,text = "O's turn",font = ("Helvetica",20,'bold') ,bg = '#ECE8DD',fg = '#0081B4')
turn_o.pack()
turn_o_frame.place(x=480,y=170)

turn_x_frame = Frame(main_frame)
turn_x = Label(turn_x_frame,text = "X's turn",font = ("Helvetica",20,'bold') ,bg = '#ECE8DD',fg = '#0081B4')
turn_x.pack()
turn_x_frame.place(x=480,y=170)


game_lab = Label(main_frame,text = "Game:1 ",font = ("Helvetica",20,'bold'),bg = '#ECE8DD',fg = '#0081B4')
game_lab.place(x=400,y=120)

turn_lab = Label(main_frame,text = "Turn: ",font = ("Helvetica",20,'bold'),bg = '#ECE8DD',fg = '#0081B4')
turn_lab.place(x=400,y=170)

move_lab = Label(main_frame,text = "Moves : 0",font = ("Helvetica",20,'bold'),bg = '#ECE8DD',fg = '#0081B4')
move_lab.place(x=400,y=220)
#No. Of O Wins
x_lab = Label(main_frame,text = "No. Of X Wins : 0",font = ("Helvetica",20,'bold'),bg = '#ECE8DD',fg = '#0081B4')
x_lab.place(x=400,y=270)

o_lab = Label(main_frame,text = "No. Of O Wins : 0",font = ("Helvetica",20,'bold'),bg = '#ECE8DD',fg = '#0081B4')
o_lab.place(x=400,y=320)

t_lab = Label(main_frame,text = "No. Of ties : 0",font = ("Helvetica",20,'bold'),bg = '#ECE8DD',fg = '#0081B4')
t_lab.place(x=400,y=370)
# Buttons to click the x's or the o's 

reset()


# 5) statistics screen 

stats = Frame(root,width = 700, height = 450,bg = '#ECE8DD')
stats.place(x=0,y=0)
decoration_6 = Frame(stats,width = 700,height = 70,bg = '#579BB1')
decoration_6.place(x=0,y=0)
back_btn1 = Button(stats,text = '< back',font = ("Helvetica",15),bg = '#ECE8DD',fg = '#0081B4',command = back_to_game)
back_btn1.place(x=20,y=17)
txt = Label(stats,text = 'Statistics',font = my_font_2,fg = '#ECE8DD',bg = '#579BB1')
txt.place(x=300,y=20)

# Buttons to click the x's or the o's 

reset()


# 7 ) Account settings 

accounts = Frame(root,width = 700, height = 450,bg = '#ECE8DD')
accounts.place(x=0, y=0)
decoration_4 = Frame(accounts,width = 700,height = 80,bg = '#579BB1')
decoration_4.place(x=0,y=0)
back_btn3 = Button(accounts,text = '< back',font = ("Helvetica",15),bg = '#ECE8DD',fg = '#0081B4',command = back_to_game)
back_btn3.place(x=14,y=25)
txt1 = Label(accounts,text = 'Account Settings',font = my_font_2,fg = '#ECE8DD',bg = '#579BB1')
txt1.place(x=240,y=20)

option_1 = Button(accounts,text = "Change Username",font=("Arial",20),command = change_username,fg = '#ECE8DD',bg = '#579BB1')
option_2 = Button(accounts,text = "Change Password",font=("Arial",20),command = change_password,fg = '#ECE8DD',bg = '#579BB1')
option_3 = Button(accounts,text = "Delete Account",font=("Arial",20), command = delete_account,fg = '#ECE8DD',bg = '#579BB1')

option_1.place(x=20,y=100)
option_2.place(x=20,y=200)
option_3.place(x=20,y=300)
test_frame = Frame(accounts,width = 300,height=300,background='#ECE8DD')
test_frame.place(x=350,y=100)
test_lab = Label(test_frame,text='Please click on the Buttons \n to the left.',font = ("Helvetica",17),bg = '#ECE8DD',fg = '#0081B4')
test_lab.place(x=5,y=100)

# internal frames to open account editing options 

ch_username = Frame(root,width = 300,height=300,background='#579BB1')
ch_username.place(x=350,y=100)
back_btn4 = Button(ch_username,text = "close",font = ("Helvetica",14),bg = '#ECE8DD',fg = '#0081B4',command = to_edit_acc)
back_btn4.place(x=10,y=10)
old_user = Label(ch_username,text = "Enter current Username : ", font = ("Helvetica",15),fg = '#ECE8DD',bg = '#579BB1')
old_user.place(x=10,y=60)
old_user_enter = Entry(ch_username,font = ("Helvetica",15),bg = '#ECE8DD',fg = '#0081B4')
old_user_enter.place(x=10,y=100)
new_user = Label(ch_username,text = "New Username : ", font = ("Helvetica",15),fg = '#ECE8DD',bg = '#579BB1')
new_user.place(x=10,y=160)
new_user_enter = Entry(ch_username,font = ("Helvetica",15),bg = '#ECE8DD',fg = '#0081B4')
new_user_enter.place(x=10,y=200)
submit_user = Button(ch_username,font = ("Helvetica",15),text = 'Submit',command = change_username_permanant,bg = '#ECE8DD',fg = '#0081B4')
submit_user.place(x=100,y=250)


ch_password = Frame(root,width = 300,height=300,background='#579BB1')
ch_password.place(x=350,y=100)
back_btn5 = Button(ch_password,text = "close",font = ("Helvetica",14),bg = '#ECE8DD',fg = '#0081B4',command = to_edit_acc)
back_btn5.place(x=10,y=10)
old_user_2 = Label(ch_password,text = "Enter current Username : ", font = ("Helvetica",15),fg = '#ECE8DD',bg = '#579BB1')
old_user_2.place(x=10,y=60)
old_user_2_enter = Entry(ch_password,font = ("Helvetica",15),bg = '#ECE8DD',fg = '#0081B4')
old_user_2_enter.place(x=10,y=100)
new_pass = Label(ch_password,text = "New Password : ", font = ("Helvetica",15),fg = '#ECE8DD',bg = '#579BB1')
new_pass.place(x=10,y=160)
new_pass_enter = Entry(ch_password,font = ("Helvetica",15),bg = '#ECE8DD',fg = '#0081B4')
new_pass_enter.place(x=10,y=200)
submit_pass = Button(ch_password,font = ("Helvetica",15),text = 'Submit',command = change_password_permanant,bg = '#ECE8DD',fg = '#0081B4')
submit_pass.place(x=100,y=250)

del_acc = Frame(root,width = 300,height=300,background='#579BB1')
del_acc.place(x=350,y=100)
back_btn6 = Button(del_acc,text = "close",font = ("Helvetica",14),bg = '#ECE8DD',fg = '#0081B4',command = to_edit_acc)
back_btn6.place(x=10,y=10)
old_user_3 = Label(del_acc,text = "Enter current Username : ", font = ("Helvetica",15),fg = '#ECE8DD',bg = '#579BB1')
old_user_3.place(x=10,y=60)
old_user_3_enter = Entry(del_acc,font = ("Helvetica",15),bg = '#ECE8DD',fg = '#0081B4')
old_user_3_enter.place(x=10,y=100)
del_txt1 = Label(del_acc,text = "Are you sure you want to delete",font = ("Helvetica",15) ,fg = '#ECE8DD',bg = '#579BB1')
del_txt2 = Label(del_acc,text = "your account ?",font = ("Helvetica",15) ,fg = '#ECE8DD',bg = '#579BB1')
del_txt1.place(x=10,y=150)
del_txt2.place(x=85,y=177)

confirm_btn_1 = Button(del_acc,font = ("Helvetica",15),text = 'Confirm',command = delete_acc_permanant,bg = '#ECE8DD',fg = '#0081B4')
confirm_btn_1.place(x=100,y=250)

disable_btn()
home_frame.tkraise()


mainloop()