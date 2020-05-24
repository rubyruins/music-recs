from tkinter import *
import tkinter as tkinter
import pandas as pd   #to extract data from exel
import Recommenders

def popnum(T,pop):
   num=0
   try:
      num = int(T.get("1.0", "end"))
      scrollbar = Scrollbar(pop)
      scrollbar.pack(side=RIGHT, fill=Y)
      # import dataset
      dataset = pd.read_csv("songs_merged_20000.csv")
      mylist = Listbox(pop, yscrollcommand=scrollbar.set, bg="#28373c", fg="white",
                       font=("times new roman", 16, "italic"))
      pm = Recommenders.popularity_recommender_py()
      pm.create(dataset, 'user_id', 'name')
      X = pm.recommend(num).values
      print("___________________________________________________________")
      for i in range(10):
          mylist.insert(END, "Trending #",(i+1),"Record title:",X[i][0],"No. of hits:",X[i][1])
          mylist.insert(END, "-----------------------------------------------------------------------")

      print(mylist)
      mylist.place(x=20, y=85, width=450, height=545)
      scrollbar.config(command=mylist.yview, background="#28373c")
   except:
      T.insert(END,"Enter integer only")

def popularity():
   pop=Tk()
   pop.config(background="#28373c")
   pop.title("Top songs")
   pop.geometry("500x650")

   background = LabelFrame(pop, text="Trending songs of the week",font=("times new roman", 15, "italic"),fg="white",bg="#28373c")
   background.place(x=10, y=10, width=480, height=630)
   T = Text(pop, height=1, width=35, font=("times new roman", 15))
   T.place(x=30, y=40)
   T.insert(END, "Enter Number of Songs ")
   btn1 = Button(pop, text='Search', bg="#28373c", command=lambda: popnum(T, pop), fg="white")
   btn1.place(x=410, y=40, height=40, width=60)

   pop.mainloop()
   
def sim(T,pop):
   song_id=T.get("1.0", "end")
   l = list(song_id.split(","))
   scrollbar = Scrollbar(pop)
   scrollbar.pack(side=RIGHT, fill=Y)
   print("heloo")
   # import dataset
   dataset = pd.read_csv("songs_merged_20000.csv")
   mylist = Listbox(pop, yscrollcommand=scrollbar.set, bg="#28373c", fg="white", font=("times new roman", 16, "italic"))
   is_model = Recommenders.item_similarity_recommender_py()
   is_model.create(dataset, 'user_id', 'name')
   df = is_model.get_similar_items(l)
   X = df.values
   print("___________________________________________________________")
   for i in range(len(df)):
      mylist.insert(END, (i+1), X[i][1], X[i][2])
      mylist.insert(END, "______________________________________________________________")

   print(mylist)
   mylist.place(x=20, y=155, width=450, height=480)
   scrollbar.config(command=mylist.yview, background="#28373c")

def similar():
   print("helo")
   pop = Tk()
   pop.config(background="#28373c")
   pop.title("Similar songs")
   pop.geometry("500x650")

   background = LabelFrame(pop, text="Songs matching to your taste of listening", font=("times new roman",18, "bold"), fg="white",
                           bg="#28373c")
   background.place(x=10, y=10, width=480, height=630)
   background = Label(pop, text="⬖ Enter songs you like",font=("times new roman", 15, "bold"), fg="white",bg="#28373c")
   background.place(x=20, y=50, width=200, height=30)
   T = Text(pop, height=2, width=38,font=("times new roman", 15))
   T.place(x=20,y=100)
   T.insert(END, "enter here")
   btn1 = Button(pop, text='Search', bg="#28373c",command=lambda :sim(T,pop),fg="white")
   btn1.place(x=410, y=100,height=50,width=70)

   pop.mainloop()

   
if __name__ == "__main__":
   # create a GUI window
   root = tkinter.Toplevel()
   root.configure(background="black")

   # set the title of GUI window
   root.title("Songrec")

   # set the configuration of GUI window
   root.geometry("750x850")  #500x700
   filename = PhotoImage(file="wallpaperr.PNG")
   background_label = Label(root, image=filename)
   background_label.place(x=0, y=0, relwidth=1, relheight=1)

   trackframe = Label(root, text="  Welcome back, Music Lover! ", font=("times new roman", 25, "bold"), bg="#28373c", fg="white",
                           bd=1)
   trackframe.place(x=10, y=20, width=430, height=50)
   file = PhotoImage(file="button1.PNG")
   btn1 = Button(root, text='Top Songs' ,image=file,command=popularity)
   btn1.place(x=50,y=100)

   file1 = PhotoImage(file="button2.PNG")
   btn2 = Button(root, text='smilar', image=file1,command=similar)
   btn2.place(x=250, y=340)


   track = Label(root, text="  Music is a piece of art which goes straight from ears to the heart..", font=("times new roman", 18, "italic"), bg="#28373c",
                      fg="white",
                      bd=1)
   track.place(x=15, y=755, width=640, height=50)
   
   root.mainloop()
