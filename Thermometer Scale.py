from tkinter import*

def submit():
    print("The temperature is: " + str(scale.get()) + " degrees Celsius")
    
window = Tk()

hotImage = PhotoImage(file = 'fire.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window, 
        from_= 100, 
        to = 0, 
        length = 600, 
        orient = VERTICAL, #orientation of the scale
        font_ = ('Consolas', 20),
        tickinterval = 10, #adds numeric indicators for value
        #resolution = 5 increment of slide
        troughcolor ='#FFDEAD', #color of slider surface
        fg = 'black',
        bg= 'white'

        )
scale.set(150) #sets the location of slider
scale.pack()

coldImage = PhotoImage(file = 'ice.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window, text = 'submit', command=submit)
button.pack()

window.mainloop()