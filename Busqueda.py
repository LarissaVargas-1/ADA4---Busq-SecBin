import tkinter as tk
from tkinter import messagebox

# ==========================================
# ALGORITMOS DE BÚSQUEDA
# ==========================================

def busqueda_secuencial(lista, objetivo):
    for indice in range(len(lista)):
        if lista[indice].lower() == objetivo.lower():
            return indice
    return -1

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def busqueda_hash(tabla, clave):
    return tabla.get(clave, None)

# ==========================================
# INTERFAZ GRÁFICA (TKINTER)
# ==========================================

class AppBusquedas:
    def __init__(self, root):
        self.root = root
        self.root.title("Métodos de Búsqueda en Python")
        self.root.geometry("540x460")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f8")

        # Estructuras vacías para que el usuario ingrese sus datos
        self.lista_secuencial = []
        self.lista_binaria = []
        self.tabla_hash = {}

        self.contenedor = tk.Frame(self.root, bg="#f0f4f8")
        self.contenedor.pack(fill="both", expand=True, padx=20, pady=20)

        self.mostrar_menu()

    def limpiar_pantalla(self):
        for widget in self.contenedor.winfo_children():
            widget.destroy()

    # --- MENÚ PRINCIPAL ---
    def mostrar_menu(self):
        self.limpiar_pantalla()

        tk.Label(self.contenedor, text="MÉTODOS DE BÚSQUEDA", font=("Arial", 16, "bold"), bg="#f0f4f8", fg="#1e293b").pack(pady=(15, 5))
        tk.Label(self.contenedor, text="Selecciona el método que deseas utilizar:", font=("Arial", 10), bg="#f0f4f8", fg="#475569").pack(pady=(0, 25))

        estilo_boton = {
            "font": ("Arial", 11, "bold"),
            "width": 32,
            "pady": 10,
            "bd": 0,
            "cursor": "hand2",
            "fg": "white"
        }

        tk.Button(self.contenedor, text="1. Búsqueda Secuencial", bg="#2563eb", command=self.vista_secuencial, **estilo_boton).pack(pady=8)
        tk.Button(self.contenedor, text="2. Búsqueda Binaria", bg="#0d9488", command=self.vista_binaria, **estilo_boton).pack(pady=8)
        tk.Button(self.contenedor, text="3. Búsqueda Hash", bg="#7c3aed", command=self.vista_hash, **estilo_boton).pack(pady=8)
        tk.Button(self.contenedor, text="Salir", font=("Arial", 10, "bold"), width=15, pady=6, bg="#dc2626", fg="white", bd=0, cursor="hand2", command=self.root.quit).pack(pady=(30, 0))

    # --- 1. BÚSQUEDA SECUENCIAL ---
    def vista_secuencial(self):
        self.limpiar_pantalla()

        tk.Label(self.contenedor, text="1. Búsqueda Secuencial", font=("Arial", 14, "bold"), bg="#f0f4f8", fg="#2563eb").pack(pady=5)
        tk.Label(self.contenedor, text="Ingresar dato a la lista:", font=("Arial", 9, "bold"), bg="#f0f4f8").pack(pady=(5, 2))

        frame_agregar = tk.Frame(self.contenedor, bg="#f0f4f8")
        frame_agregar.pack()

        entrada_nuevo = tk.Entry(frame_agregar, font=("Arial", 10), width=22)
        entrada_nuevo.pack(side="left", padx=5)

        lbl_lista = tk.Label(self.contenedor, text=f"Datos: {self.lista_secuencial}", font=("Arial", 9), bg="#e2e8f0", padx=10, pady=5, wraplength=450)
        lbl_lista.pack(pady=8)

        def agregar():
            dato = entrada_nuevo.get().strip()
            if not dato:
                messagebox.showwarning("Aviso", "Escribe un dato para agregar.")
                return
            self.lista_secuencial.append(dato)
            entrada_nuevo.delete(0, tk.END)
            lbl_lista.config(text=f"Datos: {self.lista_secuencial}")

        tk.Button(frame_agregar, text="+ Agregar", font=("Arial", 9, "bold"), bg="#16a34a", fg="white", bd=0, padx=10, pady=3, cursor="hand2", command=agregar).pack(side="left")

        tk.Label(self.contenedor, text="Dato a buscar:", font=("Arial", 10, "bold"), bg="#f0f4f8").pack(pady=(12, 2))
        entrada_buscar = tk.Entry(self.contenedor, font=("Arial", 11), width=28, justify="center")
        entrada_buscar.pack(pady=5)

        lbl_resultado = tk.Label(self.contenedor, text="", font=("Arial", 10, "bold"), bg="#f0f4f8")
        lbl_resultado.pack(pady=10)

        def buscar():
            if not self.lista_secuencial:
                messagebox.showwarning("Lista vacía", "Primero ingresa datos a la lista.")
                return
            objetivo = entrada_buscar.get().strip()
            if not objetivo:
                messagebox.showwarning("Aviso", "Escribe el dato que deseas buscar.")
                return
            pos = busqueda_secuencial(self.lista_secuencial, objetivo)
            if pos != -1:
                lbl_resultado.config(text=f"✅ '{objetivo}' encontrado en el índice {pos}.", fg="#16a34a")
            else:
                lbl_resultado.config(text=f"❌ '{objetivo}' no se encuentra en la lista.", fg="#dc2626")

        tk.Button(self.contenedor, text="Buscar", font=("Arial", 10, "bold"), bg="#2563eb", fg="white", padx=20, pady=6, bd=0, cursor="hand2", command=buscar).pack(pady=5)
        tk.Button(self.contenedor, text="← Volver al Menú", font=("Arial", 9), bg="#64748b", fg="white", padx=10, pady=4, bd=0, cursor="hand2", command=self.mostrar_menu).pack(pady=10)

    # --- 2. BÚSQUEDA BINARIA ---
    def vista_binaria(self):
        self.limpiar_pantalla()

        tk.Label(self.contenedor, text="2. Búsqueda Binaria", font=("Arial", 14, "bold"), bg="#f0f4f8", fg="#0d9488").pack(pady=5)
        tk.Label(self.contenedor, text="Ingresar número (se ordena automáticamente):", font=("Arial", 9, "bold"), bg="#f0f4f8").pack(pady=(5, 2))

        frame_agregar = tk.Frame(self.contenedor, bg="#f0f4f8")
        frame_agregar.pack()

        entrada_nuevo = tk.Entry(frame_agregar, font=("Arial", 10), width=22)
        entrada_nuevo.pack(side="left", padx=5)

        lbl_lista = tk.Label(self.contenedor, text=f"Datos ordenados: {self.lista_binaria}", font=("Arial", 9), bg="#e2e8f0", padx=10, pady=5, wraplength=450)
        lbl_lista.pack(pady=8)

        def agregar():
            try:
                num = int(entrada_nuevo.get().strip())
                self.lista_binaria.append(num)
                self.lista_binaria.sort()
                entrada_nuevo.delete(0, tk.END)
                lbl_lista.config(text=f"Datos ordenados: {self.lista_binaria}")
            except ValueError:
                messagebox.showerror("Error", "Ingresa solo números enteros.")

        tk.Button(frame_agregar, text="+ Agregar", font=("Arial", 9, "bold"), bg="#16a34a", fg="white", bd=0, padx=10, pady=3, cursor="hand2", command=agregar).pack(side="left")

        tk.Label(self.contenedor, text="Número a buscar:", font=("Arial", 10, "bold"), bg="#f0f4f8").pack(pady=(12, 2))
        entrada_buscar = tk.Entry(self.contenedor, font=("Arial", 11), width=28, justify="center")
        entrada_buscar.pack(pady=5)

        lbl_resultado = tk.Label(self.contenedor, text="", font=("Arial", 10, "bold"), bg="#f0f4f8")
        lbl_resultado.pack(pady=10)

        def buscar():
            if not self.lista_binaria:
                messagebox.showwarning("Lista vacía", "Primero ingresa números a la lista.")
                return
            try:
                objetivo = int(entrada_buscar.get().strip())
                pos = busqueda_binaria(self.lista_binaria, objetivo)
                if pos != -1:
                    lbl_resultado.config(text=f"✅ {objetivo} encontrado en el índice {pos}.", fg="#16a34a")
                else:
                    lbl_resultado.config(text=f"❌ {objetivo} no se encuentra en la lista.", fg="#dc2626")
            except ValueError:
                messagebox.showerror("Error", "Ingresa un número entero válido.")

        tk.Button(self.contenedor, text="Buscar", font=("Arial", 10, "bold"), bg="#0d9488", fg="white", padx=20, pady=6, bd=0, cursor="hand2", command=buscar).pack(pady=5)
        tk.Button(self.contenedor, text="← Volver al Menú", font=("Arial", 9), bg="#64748b", fg="white", padx=10, pady=4, bd=0, cursor="hand2", command=self.mostrar_menu).pack(pady=10)

    # --- 3. BÚSQUEDA HASH ---
    def vista_hash(self):
        self.limpiar_pantalla()

        tk.Label(self.contenedor, text="3. Búsqueda Hash", font=("Arial", 14, "bold"), bg="#f0f4f8", fg="#7c3aed").pack(pady=5)
        tk.Label(self.contenedor, text="Ingresar Clave y Valor:", font=("Arial", 9, "bold"), bg="#f0f4f8").pack(pady=(5, 2))

        frame_agregar = tk.Frame(self.contenedor, bg="#f0f4f8")
        frame_agregar.pack()

        tk.Label(frame_agregar, text="Clave:", font=("Arial", 9), bg="#f0f4f8").pack(side="left")
        entrada_clave = tk.Entry(frame_agregar, font=("Arial", 9), width=12)
        entrada_clave.pack(side="left", padx=4)

        tk.Label(frame_agregar, text="Valor:", font=("Arial", 9), bg="#f0f4f8").pack(side="left")
        entrada_valor = tk.Entry(frame_agregar, font=("Arial", 9), width=16)
        entrada_valor.pack(side="left", padx=4)

        lbl_datos = tk.Label(self.contenedor, text=f"Tabla Hash: {self.tabla_hash}", font=("Arial", 9), bg="#e2e8f0", padx=10, pady=5, wraplength=450)
        lbl_datos.pack(pady=8)

        def agregar():
            clave = entrada_clave.get().strip()
            valor = entrada_valor.get().strip()
            if not clave or not valor:
                messagebox.showwarning("Aviso", "Completa ambos campos (Clave y Valor).")
                return
            self.tabla_hash[clave] = valor
            entrada_clave.delete(0, tk.END)
            entrada_valor.delete(0, tk.END)
            lbl_datos.config(text=f"Tabla Hash: {self.tabla_hash}")

        tk.Button(frame_agregar, text="+ Guardar", font=("Arial", 9, "bold"), bg="#16a34a", fg="white", bd=0, padx=8, pady=3, cursor="hand2", command=agregar).pack(side="left", padx=4)

        tk.Label(self.contenedor, text="Clave a buscar:", font=("Arial", 10, "bold"), bg="#f0f4f8").pack(pady=(12, 2))
        entrada_buscar = tk.Entry(self.contenedor, font=("Arial", 11), width=28, justify="center")
        entrada_buscar.pack(pady=5)

        lbl_resultado = tk.Label(self.contenedor, text="", font=("Arial", 10, "bold"), bg="#f0f4f8")
        lbl_resultado.pack(pady=10)

        def buscar():
            if not self.tabla_hash:
                messagebox.showwarning("Tabla vacía", "Primero guarda pares de Clave y Valor.")
                return
            clave = entrada_buscar.get().strip()
            if not clave:
                messagebox.showwarning("Aviso", "Escribe la clave que deseas buscar.")
                return
            valor = busqueda_hash(self.tabla_hash, clave)
            if valor is not None:
                lbl_resultado.config(text=f"✅ Clave '{clave}' encontrada → Valor: '{valor}'.", fg="#16a34a")
            else:
                lbl_resultado.config(text=f"❌ La clave '{clave}' no existe en la tabla hash.", fg="#dc2626")

        tk.Button(self.contenedor, text="Buscar", font=("Arial", 10, "bold"), bg="#7c3aed", fg="white", padx=20, pady=6, bd=0, cursor="hand2", command=buscar).pack(pady=5)
        tk.Button(self.contenedor, text="← Volver al Menú", font=("Arial", 9), bg="#64748b", fg="white", padx=10, pady=4, bd=0, cursor="hand2", command=self.mostrar_menu).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = AppBusquedas(root)
    root.mainloop()