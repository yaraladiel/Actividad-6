import tkinter as tk

class AppLogin:
    USUARIO_VALIDO = "medebes"
    PASSWORD_VALIDO = "5000"
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("500x500")
        self.ventana.title("Corrección de validación de credenciales")
        
        self.etiqueta_usuario = tk.Label(self.ventana, text="Usuario")
        self.etiqueta_usuario.pack()
        
        self.input_usuario = tk.Entry(self.ventana)
        self.input_usuario.pack()
        
        self.etiqueta_password = tk.Label(self.ventana, text="Password")
        self.etiqueta_password.pack()
        
        self.input_password = tk.Entry(self.ventana, show="*")
        self.input_password.pack()
        
        self.mensaje = tk.Label(self.ventana)
        self.mensaje.pack()
        
        self.boton = tk.Button(
            self.ventana, 
            text="Ingresar", 
            command=self.validar_credenciales
        )
        self.boton.pack()
    
    def validar_credenciales(self):
        usuario = self.input_usuario.get()
        password = self.input_password.get()
        
        if usuario == self.USUARIO_VALIDO and password == self.PASSWORD_VALIDO:
            self.mensaje.config(text="Acceso correcto", foreground="green")
        else:
            self.mensaje.config(text="Usuario o contraseña incorrectos", foreground="red")
    
    def ejecutar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    app = AppLogin()
    app.ejecutar()