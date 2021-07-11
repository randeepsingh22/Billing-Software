from tkinter import *
from tkinter import messagebox as msg
import random
from tkinter.filedialog import asksaveasfile
import datetime as dt
import pickle

#Rates of Items
# Bulbs
philpRate = 20
anchorBulbRate = 30
havelsBulb = 25
evereadyRate = 15
sovaRate = 18
sikhshaRate = 24
novaRate = 28

# Wires
anchorWireRate = 300
havelsWireRate = 250
fabriccoWireRate = 150
rrWireRate =175
polycabWireRate = 290
finolexWireRate = 210
syskaWireRate = 190

def genratebill():
    date = dt.datetime.now()
    t_philp = float(philips.get()) * philpRate
    t_anchor = float(anchor.get()) * anchorBulbRate
    t_havels = float(havels.get()) * havelsBulb
    t_eveready = float(eveready.get()) * evereadyRate
    t_sova = float(sova.get()) * sovaRate
    t_sikhsha = float(sikhsha.get()) * sikhshaRate
    t_nova = float(nova.get()) * novaRate
    t_anchors = float(anchors.get())*anchorWireRate
    t_havel = float(havel.get())* havelsWireRate
    t_fabricco = float(fabricco.get())* fabriccoWireRate
    t_rr = float(rr.get())* rrWireRate
    t_polycab = float(polycab.get())* polycabWireRate
    t_finolex = float(finolex.get())* finolexWireRate
    t_syska = float(syska.get())* syskaWireRate
    total = (t_philp + t_anchor + t_havels +
             t_eveready + t_sova + t_sikhsha + t_nova + t_anchors+t_havel+t_fabricco+t_rr+t_polycab+t_finolex+t_syska)
    taxpaid = (total*2)/100
    g_total = total+taxpaid
    totalbill.set(f"Rs.{str(g_total)}")
    taxpd.set(f"Rs.{str(taxpaid)}")

    txtarea.delete("1.0", "end")

    radm = random.randint(1, 200)
    c_billno.set(str(radm))
    txtarea.insert(END, "\t\t\tWelcome R.S Enterprises\n")

    txtarea.insert(
        END, "***************************************************************************************************************\n")

    txtarea.insert(END, f" Bill No: {str(radm)}\n")

    txtarea.insert(END, f" Customer Name: {cname.get().capitalize()}\n")
    txtarea.insert(END, f" Phone No: {c_phneno.get()}\n")
    txtarea.insert(END, f" Date: {date.strftime('%d-%m-%Y')}\n")

    txtarea.insert(
        END, "***************************************************************************************************************\n")

    txtarea.insert(
        END, f"         Items\t\t\t            Qty\t\t\t              Price\n")
    txtarea.insert(
        END, "***************************************************************************************************************\n")
    if philips.get() != str(0):
        txtarea.insert(
            END, f"    Philps Bulb's\t\t\t             {philips.get()[1:]}\t\t\t              {t_philp}\n")

    if anchor.get() != str(0):
        txtarea.insert(
            END, f"    Anchor Bulb's\t\t\t             {anchor.get()[1:]}\t\t\t              {t_anchor}\n")

    if havels.get() != str(0):
        txtarea.insert(
            END, f"    Havels Bulb's\t\t\t             {havels.get()[1:]}\t\t\t              {t_havels}\n")

    if eveready.get() != str(0):
        txtarea.insert(
            END, f"    Eveready\t\t\t             {eveready.get()[1:]}\t\t\t              {t_eveready}\n")

    if sova.get() != str(0):
        txtarea.insert(
            END, f"    Sova Bulb's\t\t\t             {sova.get()[1:]}\t\t\t              {t_sova}\n")

    if sikhsha.get() != str(0):
        txtarea.insert(
            END, f"    Sikhsha Bulb's\t\t\t             {sikhsha.get()[1:]}\t\t\t              {t_sikhsha}\n")

    if nova.get() != str(0):
        txtarea.insert(
            END, f"    Nova Bulb's\t\t\t             {nova.get()[1:]}\t\t\t              {t_nova}\n")
    if anchors.get() != str(0):
        txtarea.insert(
            END, f"    Anchor Wire\t\t\t             {anchors.get()[1:]}\t\t\t              {t_anchors}\n")
    if havel.get() != str(0):
        txtarea.insert(
            END, f"    Havels Wire\t\t\t             {havel.get()[1:]}\t\t\t              {t_havel}\n")
    if fabricco.get() != str(0):
        txtarea.insert(
            END, f"    Fabricco Wire\t\t\t             {fabricco.get()[1:]}\t\t\t              {t_fabricco}\n")
    if rr.get() != str(0):
        txtarea.insert(
            END, f"    RR Cabels Wire\t\t\t             {rr.get()[1:]}\t\t\t              {t_rr}\n")
    if polycab.get() != str(0):
        txtarea.insert(
            END, f"    PolyCab Wire\t\t\t             {polycab.get()[1:]}\t\t\t              {t_polycab}\n")
    if finolex.get() != str(0):
        txtarea.insert(
            END, f"    Finolex Wire\t\t\t             {finolex.get()[1:]}\t\t\t              {t_finolex}\n")
    if syska.get() != str(0):
        txtarea.insert(
            END, f"    Syska Wire\t\t\t             {syska.get()[1:]}\t\t\t              {t_syska}\n")

    txtarea.insert(
        END, "***************************************************************************************************************\n")
    txtarea.insert(
        END, f"                                                                                                    \t\tTotal = Rs.{str(total)}\n")
    txtarea.insert(
        END, "***************************************************************************************************************\n")
    textarea = txtarea.get("1.0", "end")


def exit():
    permission = msg.askquestion(
        "Exit", "All Your Data will be removed permanently from the Window.\n                               Do you want to Exit?")

    if permission == "yes":
        root.destroy()


def genrateBill():
    date = dt.datetime.now()
    if cname.get() == "" and c_phneno.get() == "":
        msg.showinfo(
            "Warning", "Please fill your Name and Phone Number in the Above Fields.")
    elif cname.get() == "":
        msg.showinfo("Warning", "Please! Enter Your Name.")
    elif c_phneno.get() == "":
        msg.showinfo("Warning", "Please! Enter Your Phone Number.")
    elif philips.get() == str(0) and anchor.get() == str(0) and havel.get() == str(0) and sova.get() == str(0) and eveready.get() == str(0) and sikhsha.get() == str(0) and nova.get() == str(0) and anchors.get() == str(0) and havel.get() == str(0) and fabricco.get() == str(0) and rr.get() == str(0) and polycab.get() == str(0) and finolex.get() == str(0) and syska.get() == str(0):
        msg.showinfo(
            "Warning", "Please! Enter atleast One items in the Given Field's in order Genrate Bill.")
    elif len(c_phneno.get()) < 10:
        msg.showinfo("Warning", "Phone number Should be atleast of 10 Digits.")
    elif len(c_phneno.get()) > 10:
        msg.showinfo("Warning", "Phone number Should be of 10 Digits.")
    else:
        permission = msg.askquestion("Save", "Do You want to save The File?")
        if permission == "yes":
            genratebill()
            text = txtarea.get(1.0, END)
            with open("Billing Data.txt", "a") as f:
                f.write(text)
        else:
            genratebill()


def clear():
    # customer details
    txtarea.delete("1.0", "end")
    cname.set("")
    c_phneno.set("")
    c_billno.set(0)

    # bulbs
    totalbill.set("Rs."+str(0))
    taxpd.set("Rs."+str(0))
    philips.set(0)
    anchor.set(0)
    havels.set(0)
    eveready.set(0)
    sova.set(0)
    sikhsha.set(0)
    nova.set(0)
    # wires
    anchors.set(0)
    havel.set(0)
    fabricco.set(0)
    rr.set(0)
    polycab.set(0)
    finolex.set(0)
    syska.set(0)
    DefaultBillArea()


def total():
    try:
        permission = msg.askquestion(
            "Total", "Do You want to Total the Given Items.")
        if permission == "yes":
            if philips.get() == str(0) and anchor.get() == str(0) and havel.get() == str(0) and sova.get() == str(0) and eveready.get() == str(0) and sikhsha.get() == str(0) and nova.get() == str(0) and anchors.get() == str(0) and havel.get() == str(0) and fabricco.get() == str(0) and rr.get() == str(0) and polycab.get() == str(0) and finolex.get() == str(0) and syska.get() == str(0):
                msg.showinfo(
                    "Warning", "Please! Enter atleast One items in the Given Field.")
            else:
                t_philp = float(philips.get()) * philpRate
                t_anchor = float(anchor.get()) * anchorBulbRate
                t_havels = float(havels.get()) * havelsBulb
                t_eveready = float(eveready.get()) * evereadyRate
                t_sova = float(sova.get()) * sovaRate
                t_sikhsha = float(sikhsha.get()) * sikhshaRate
                t_nova = float(nova.get()) * novaRate
                t_anchors = float(anchors.get())*anchorWireRate
                t_havel = float(havel.get())* havelsWireRate
                t_fabricco = float(fabricco.get())* fabriccoWireRate
                t_rr = float(rr.get())* rrWireRate
                t_polycab = float(polycab.get())* polycabWireRate
                t_finolex = float(finolex.get())* finolexWireRate
                t_syska = float(syska.get())* syskaWireRate
                total = (t_philp + t_anchor + t_havels +
                         t_eveready + t_sova + t_sikhsha + t_nova + t_anchors+t_havel+t_fabricco+t_rr+t_polycab+t_finolex+t_syska)
                taxpaid = (total*2)/100
                g_total = total+taxpaid
                totalbill.set(f"Rs.{str(g_total)}")
                taxpd.set(f"Rs.{str(taxpaid)}")
    except:
        msg.showinfo("Warning", "Please Enter Number Only.")


root = Tk()


def DefaultBillArea():
    date = dt.datetime.now()
    txtarea.insert(END, "\t\t\tWelcome R.S Enterprises\n")
    txtarea.insert(
        END, "***************************************************************************************************************\n")
    txtarea.insert(END, f" Bill No: \n")
    txtarea.insert(END, f" Customer Name: \n")
    txtarea.insert(END, f" Phone No: \n")
    txtarea.insert(END, f" Date: {date.strftime('%d-%m-%Y')}\n")
    txtarea.insert(
        END, "***************************************************************************************************************\n")
    txtarea.insert(
        END, f"         Items\t\t\t            Qty\t\t\t               Price\n")
    txtarea.insert(
        END, "***************************************************************************************************************\n")
    txtarea.insert(END, f"")


cname = StringVar()
c_phneno = StringVar()
c_billno = IntVar()

# Bulbs

philips = StringVar()
anchor = StringVar()
havels = StringVar()
eveready = StringVar()
sova = StringVar()
sikhsha = StringVar()
nova = StringVar()

# wires

anchors = StringVar()
havel = StringVar()
fabricco = StringVar()
rr = StringVar()
polycab = StringVar()
finolex = StringVar()
syska = StringVar()
# totalbill
totalbill = StringVar()
# tax paid
taxpd = StringVar()


pl = "#006622"
root.geometry("1525x800")
root.minsize(1525,800)
root.title("Billing Software | Developed by Randeep")
Label(text="Billing Software", font=("times new roman", 24, "bold"),
      fg="gold", pady=10, bd=10, relief=GROOVE, bg=pl).pack(fill="x", pady=2)

f1 = LabelFrame(root, text="Customer Details",
                font="arial 12 bold", bg=pl, bd=10, relief=GROOVE, fg="gold")
f1.place(x=1, y=78, relwidth=1)

c_name = Label(f1, text="Customer's Name", font=("times new roman", 18, "bold"),
               bg=pl, fg="white").grid(row=0, column=0, padx=20, pady=8)
c_name = Entry(f1, font=("times new roman", 15, "bold"), bd=4, textvariable=cname,
               relief=SUNKEN).grid(row=0, column=1, padx=20, pady=8)

p_no = Label(f1, text="Phone No.", font=("times new roman", 18, "bold"), bg=pl,
             fg="white").grid(row=0, column=2, padx=20, pady=8)
p_no = Entry(f1, font=("times new roman", 15, "bold"), textvariable=c_phneno, bd=4,
             relief=SUNKEN).grid(row=0, column=3, padx=20, pady=8)

b_bill = Label(f1, text="Bill No.", font=("times new roman", 18, "bold"), bg=pl,
               fg="white").grid(row=0, column=4, padx=20, pady=8)
b_bill = Entry(f1, font="Arial 15 bold", textvariable=c_billno,
               bd=4, relief=SUNKEN).grid(row=0, column=5, padx=20, pady=8)

Button(f1, text="Search", font="lucida 16 bold", bd=2,
       padx=10).grid(row=0, column=6, padx=20, pady=8)

f2 = LabelFrame(root, text="Categories of Bulb's",
                font="arial 12 bold", bg=pl, bd=10, relief=GROOVE, fg="gold")
f2.place(x=1, y=170, width=350, height=400)

philp_lbl = Label(f2, text="Philips", font="arial 15 ", fg="yellow", bg=pl).grid(
    row=0, column=0, padx=8, pady=12, sticky="w")
philp_entry = Entry(f2, bd=5, relief=SUNKEN, textvariable=philips,
                    font="arial 10 bold").grid(row=0, column=1, padx=15, pady=12)

anchor_lbl = Label(f2, text="Anchor", font="arial 15 ", fg="yellow", bg=pl).grid(
    row=2, column=0, padx=8, pady=12, sticky="w")
anchor_entry = Entry(f2, bd=5, relief=SUNKEN, textvariable=anchor,
                     font="arial 10 bold").grid(row=2, column=1, padx=15, pady=12)

havels_lbl = Label(f2, text="Havels", font="arial 15", fg="yellow", bg=pl).grid(
    row=3, column=0, padx=8, pady=12, sticky="w")
havels_entry = Entry(f2, bd=5, relief=SUNKEN, font="arial 10 bold",
                     textvariable=havels).grid(row=3, column=1, padx=15, pady=12)

sova_lbl = Label(f2, text="Sova", font="arial 15", fg="yellow", bg=pl).grid(
    row=4, column=0, padx=8, pady=12, sticky="w")
sova_entry = Entry(f2, bd=5, relief=SUNKEN, font="arial 10 bold",
                   textvariable=sova).grid(row=4, column=1, padx=15, pady=12)

everrdy_lbl = Label(f2, text="Eveready", font="arial 15", fg="yellow", bg=pl).grid(
    row=5, column=0, padx=8, pady=12, sticky="w")
everrdy_entry = Entry(f2, bd=5, relief=SUNKEN, font="arial 10 bold",
                      textvariable=eveready).grid(row=5, column=1, padx=15, pady=12)

sikhsha_lbl = Label(f2, text="Sikhsha", font="arial 15", fg="yellow", bg=pl).grid(
    row=6, column=0, padx=8, pady=12, sticky="w")
sikhsha_entry = Entry(f2, bd=5, relief=SUNKEN, font="arial 10 bold",
                      textvariable=sikhsha).grid(row=6, column=1, padx=15, pady=12)

nova_lbl = Label(f2, text="Nova", font="arial 15", fg="yellow", bg=pl).grid(
    row=7, column=0, padx=8, pady=12, sticky="w")
nova_entry = Entry(f2, bd=5, relief=SUNKEN, font="arial 10 bold",
                   textvariable=nova).grid(row=7, column=1, padx=15, pady=12)

f3 = LabelFrame(root, text="Wires", font="arial 12 bold",
                bg=pl, bd=10, relief=GROOVE, fg="gold")
f3.place(x=355, y=170, width=350, height=400)

anchor_lbl = Label(f3, text="Anchor", font="arial 15", fg="yellow", bg=pl).grid(
    row=0, column=0, padx=8, pady=12, sticky="w")
anchor_entry = Entry(f3, bd=5, relief=SUNKEN, font="arial 10 bold",
                     textvariable=anchors).grid(row=0, column=1, padx=15, pady=12)

havels_lbl = Label(f3, text="Havels", font="arial 15", fg="yellow", bg=pl).grid(
    row=1, column=0, padx=8, pady=12, sticky="w")
havels_entry = Entry(f3, bd=5, relief=SUNKEN, font="arial 10 bold",
                     textvariable=havel).grid(row=1, column=1, padx=15, pady=12)

fabricco_lbl = Label(f3, text="Fabricco", font="arial 15", fg="yellow", bg=pl).grid(
    row=2, column=0, padx=8, pady=12, sticky="w")
fabricco_entry = Entry(f3, bd=5, relief=SUNKEN, font="arial 10 bold",
                       textvariable=fabricco).grid(row=2, column=1, padx=15, pady=12)

rr_lbl = Label(f3, text="RR Cabel", font="arial 15", fg="yellow", bg=pl).grid(
    row=3, column=0, padx=8, pady=12, sticky="w")
rr_entry = Entry(f3, bd=5, relief=SUNKEN, font="arial 10 bold",
                 textvariable=rr).grid(row=3, column=1, padx=15, pady=12)

polycab_lbl = Label(f3, text="PolyCab", font="arial 15", fg="yellow", bg=pl).grid(
    row=4, column=0, padx=8, pady=12, sticky="w")
polycab_entry = Entry(f3, bd=5, relief=SUNKEN, font="arial 10 bold",
                      textvariable=polycab).grid(row=4, column=1, padx=15, pady=12)

finolex_lbl = Label(f3, text="Finolex", font="arial 15", fg="yellow", bg=pl).grid(
    row=5, column=0, padx=8, pady=12, sticky="w")
finolex_entry = Entry(f3, bd=5, relief=SUNKEN, font="arial 10 bold",
                      textvariable=finolex).grid(row=5, column=1, padx=15, pady=12)

syska_lbl = Label(f3, text="Syska", font="arial 15", fg="yellow", bg=pl).grid(
    row=6, column=0, padx=8, pady=12, sticky="w")
syska_entry = Entry(f3, bd=5, relief=SUNKEN, font="arial 10 bold",
                    textvariable=syska).grid(row=6, column=1, padx=15, pady=12)

f4 = Frame(root, bg="white", bd=10, relief=GROOVE)
f4.place(x=710, y=170, width=820, height=400)

Label(f4, text="Bill Area", font=("times new roman", 24, "bold"),
      pady=5, bd=8, relief=GROOVE, fg="black").pack(fill="x")

scroll = Scrollbar(f4, orient=VERTICAL)
txtarea = Text(f4, font="lucida 14", yscrollcommand=scroll.set)
scroll.pack(fill=Y, side=RIGHT)
scroll.config(command=txtarea.yview)
txtarea.pack(fill="both", expand=1)


f5 = Frame(root, bg=pl, bd=10, relief=GROOVE)
f5.place(x=1, y=572, relwidth=1)

t_lbl = Label(f5, text="Total", font="Arial 18 bold", fg="gold", bg=pl).grid(
    row=0, column=0, padx=30, pady=10, sticky="w")
t_entry = Entry(f5, font="arial 12 bold", bd=6, relief=SUNKEN, textvariable=totalbill).grid(
    row=0, column=1, padx=20, pady=10)

tax_lbl = Label(f5, text="Tax Paid", font="Arial 18 bold", fg="gold", bg=pl).grid(
    row=1, column=0, padx=30, pady=10, sticky="w")
tax_entry = Entry(f5, font="arial 12 bold", bd=6, relief=SUNKEN, textvariable=taxpd).grid(
    row=1, column=1, padx=20, pady=10)

f6 = Frame(f5, bg=pl, bd=10, relief=GROOVE)
f6.place(x=450, width=1050, height=108)

total_btn = Button(f6, text="Total", font="Arial 15 bold", width=14, fg="black",
                   bd=7, relief=GROOVE, command=total).grid(row=0, column=0, padx=30, pady=20, sticky="w")

clear_btn = Button(f6, text="Clear", font="Arial 15 bold", fg="black", width=14,
                   bd=7, relief=GROOVE, command=clear).grid(row=0, column=1, padx=30, pady=20, sticky="w")

genrate_btn = Button(f6, text="Genrate Bill", font="Arial 15 bold", fg="black",
                     width=14, bd=7, relief=GROOVE, command=genrateBill).grid(row=0, column=2, padx=30, pady=20, sticky="w")

exit_btn = Button(f6, text="Exit", font="Arial 15 bold", fg="black", width=14,
                  bd=7, relief=GROOVE, command=exit).grid(row=0, column=3, padx=30, pady=20, sticky="w")


f7 = Frame(root, bg=pl)
f7.place(x=1, y=705, relwidth=1)

note__lbl = Label(f7, text="Note: The Rates of the listed items had already been Saved in the Database.",
                  fg="red", bg=pl, font="lucida 20 bold", pady=30).pack()

clear()
root.mainloop()
