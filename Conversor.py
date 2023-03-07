'''
Crea un programa en Python llamado Conversor.py que cree una ventana con Tkinter para convertir valores 
monetarios entre divisas Euro - Dólar y viceversa. 
1. La ventana llevará el título "Conversor Euro -  Dólar USA" y una imagen como logo de la aplicación. 
2. Se introducirá una cantidad de dinero, se indicará de qué divisa se trata y se convertirá a la otra divisa. 
3. La ventana tendrá una etiqueta principal centrada en la parte superior de la ventana cuyo texto será 
"Conversión de divisas Euro - Dólar USA". 
4. Abajo, habrá una etiqueta cuyo texto será Cantidad a convertir. A su derecha se introducirá un Cuadro 
de texto para escribir la cantidad de dinero a convertir a la otra divisa.  
5. Debajo, habrá una etiqueta con texto "Conversión" y 2 radiobutton que permitan seleccionar a qué divisa 
se quiere convertir la cantidad indicada. Esta conversión será de Euro a Dólar USA o de Dólar USA a Euro. 
6. Los cambios que se aplican en marzo de 2023 son los siguientes:  
1 dólar USA = 0,947983 euros         1 Euro = 1,054883 Dólares USA 
7. Se introducirá un botón con texto Convertir que realizará el cambio de divisa requerido y mostrará el 
resultado en otra etiqueta. Habrá una etiqueta con texto “Valor de la conversión” y a su derecha otra 
etiqueta donde se indicará el resultado numérico del cambio y en qué divisa se ha convertido. 
8. Una vez que tengas la ventana ajustada a su contenido, no permitas que se pueda redimensionar. 
'''

import tkinter as tk

class Conversor:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor Euro - Dólar USA")
        self.root.resizable(False, False)
        self.root.configure(bg = "#222222")
        
        self.logo = tk.PhotoImage(file = "money2.png")
        self.logo = self.logo.subsample(4, 4)
        tk.Label(self.root, image=self.logo, bg = "#222222").grid(row = 0, column = 0, columnspan = 4, pady = 10)
        

        tk.Label(self.root, text="Conversión de divisas Euro - Dólar USA", font=("Arial", 14), bg="#222222", fg = "white").grid(row = 1, column = 0, columnspan = 4, pady = 10)

        tk.Label(self.root, text="Cantidad a convertir:", bg= "#222222", fg= "white").grid(row = 2, column = 0, sticky = "w", padx = 10)
        self.cantTxt = tk.Entry(self.root, width = 20, bg = "white", fg = "black")
        self.cantTxt.grid(row = 2, column = 1, sticky = "w")
        self.divisa = tk.StringVar(value = "euros")


        tk.Label(self.root, text = "", bg = "#222222").grid(row = 3, column = 0, pady = 15)

        tk.Radiobutton(self.root, text="Euro a Dolar USA", variable=self.divisa, value = "euros", bg = "#222222", fg = "white", selectcolor = "#222222", activebackground = "#222222", activeforeground = "white").grid(row = 3, column = 0, sticky = "w")
        tk.Radiobutton(self.root, text="Dolar USA a Euro", variable=self.divisa, value = "dolares", bg = "#222222", fg = "white", selectcolor ="#222222", activebackground = "#222222", activeforeground = "white").grid(row = 3, column = 1, sticky = "w")

        self.convertTo = tk.StringVar(value = "dolares")
        
        tk.Button(self.root, text = "Convertir", command=self.convertir, bg = "#1e90ff", fg = "white").grid(row = 4, column = 0, columnspan = 4, pady = 10)
        
        tk.Label(self.root, text= "Valor de la conversión:", bg = "#222222", fg = "white").grid(row = 5, column = 0, sticky = "w", padx = 10)
        self.result = tk.Label(self.root, text = "", font = ("Arial", 12), bg = "#222222", fg = "white")
        self.result.grid(row = 5, column = 1, columnspan = 3)
        
    def convertir(self):

        try:
            cant = float(self.cantTxt.get())
            if cant < 0:
                self.result.config(text="Error: introduce una cantidad válida", fg = "red")
                return
        except ValueError:
            self.result.config(text="Error: introduce una cantidad válida", fg = "red")
            
        divOrigin = self.divisa.get()
        
        if divOrigin == "euros":
            res = cant * 1.054883
            divRes = "dólares"
        else:
            res = cant * 0.947983
            divRes = "euros"

        self.result.config(text=f"{res:.2f} {divRes}", fg="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = Conversor(root)
    root.mainloop()
