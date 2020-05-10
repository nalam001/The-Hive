from tkinter import *
import welcome
import viewingpage
import db
import reputationScore as repScore

class VisitorPage:

    def __init__(self):
        self.win = Tk()
        self.win.title("The Hive - Visitor Page")
        self.win.geometry('{}x{}'.format(800, 450))
        self.canvas = Canvas(self.win, bg='#454b54')

        self.pageTitle = Label(self.canvas, text="Welcome to The Hive!", bg="#454b54", fg="#f7cc35",
                               font="Arial 20 bold")
        self.topProjectsLabel = Label(self.canvas, text="Top 3 Projects", bg="#454b54", fg="white",
                               font="Arial 15 bold")
        self.topUsersLabel = Label(self.canvas, text="Top 3 User Profiles", bg="#454b54", fg="white",
                               font="Arial 15 bold")

        db.cursor.execute("SELECT username FROM thehive.users ORDER BY reputation_score DESC LIMIT 1")
        top1Name = db.cursor.fetchone()[0]
        db.cursor.execute("SELECT username FROM thehive.users ORDER BY reputation_score DESC LIMIT 1,1")
        top2Name = db.cursor.fetchone()[0]
        db.cursor.execute("SELECT username FROM thehive.users ORDER BY reputation_score DESC LIMIT 2,1")
        top3Name = db.cursor.fetchone()[0]


        self.welButton = Button(self.canvas, text="Login/Register", font='Arial 15 bold', bg='#454b54',
                                fg="#f7cc35", command=self.welcome)
        # place holder for top 3 projects
        self.project1 = Button(self.canvas, text="Project 1", font='Arial 20 bold', bg='white',
                                fg="black", width = 10, height = 2)
        self.project2 = Button(self.canvas, text="Project 2", font='Arial 20 bold', bg='white',
                                fg="black", width = 10, height = 2)
        self.project3 = Button(self.canvas, text="Project 3", font='Arial 20 bold', bg='white', fg="black", width = 10, height = 2)
        # place holder for top 3 users
        self.user1 = Button(self.canvas, text=top1Name, font='Arial 20 bold', bg='white', fg="black", width = 10, height = 2, command = lambda: self.viewingpage(top1Name))
        self.user2 = Button(self.canvas, text=top2Name, font='Arial 20 bold', bg='white', fg="black", width = 10, height = 2, command = lambda: self.viewingpage(top2Name))
        self.user3 = Button(self.canvas, text=top3Name, font='Arial 20 bold', bg='white', fg="black", width = 10, height = 2, command = lambda: self.viewingpage(top3Name))


    def main(self):
        self.canvas.pack(expand=TRUE, fill=BOTH)
        self.pageTitle.place(x = 50, y = 30)
        self.topProjectsLabel.place(x = 50, y = 90)
        self.topUsersLabel.place(x = 50, y = 285)

        self.welButton.place(x = 600, y = 30)
        self.project1.place(x = 100, y = 150)
        self.project2.place(x = 300, y = 150)
        self.project3.place(x = 500, y = 150)

        self.user1.place(x = 100, y = 325)
        self.user2.place(x = 300, y = 325)
        self.user3.place(x = 500, y = 325)

        self.win.mainloop()

    def welcome(self):
        self.win.destroy()
        wel = welcome.WelcomeWindow()
        wel.main()

    def viewingpage(self, name):
        self.win.destroy()
        view = viewingpage.viewPage(name)
        view.main()


if __name__ == "__main__":
    x = VisitorPage()
    x.main()
