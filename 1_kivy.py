from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import RiseInTransition
from kivy.uix.screenmanager import FallOutTransition
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from matplotlib import pyplot
import pandas as pd
import os

Config.set('graphics', 'fullscreen', 0)
Config.set("graphics", "resiziable", '0')
Config.set("graphics", "width", '640')
Config.set("graphics", "height", '480')
Config.write()

X=Y=H=lim=lim1=file=list_of_types=columns=key=last_version_of_graphic=False

way_to_file=''
len_columns=1000
Items = GridLayout(cols=3, rows=len_columns)
class MenuScreen(Screen):
    pass
class ChooseScreen(Screen):
    pass
class ItemsScreen(Screen):
    pass

sm = ScreenManager()
sm.transition=RiseInTransition()
MenuScreen=Screen(name='menu')
ChooseScreen=Screen(name='choose')
Items_H_Screen=Screen(name='items_h')
Items_X_Y_Screen=Screen(name='items_x_y')
sm.add_widget(MenuScreen)
sm.add_widget(ChooseScreen)
sm.add_widget(Items_H_Screen)
sm.add_widget(Items_X_Y_Screen)

class cursachApp(App):
    def build(self):

############################################################################################################
        def hist_press(self):
            global lim,lim1,X,Y,H
            if not lim and not lim1:
                if situation.text == 'Оберіть csv-файл':
                    situation.text = 'Графік обрано\nОберіть файл'
                elif situation.text == "Файл обрано\nОберіть вид графіка":
                    situation.text = 'Файл і графік обрано\nОберіть значення'
                full_interface.add_widget(hist)
                lim = True
            elif not lim and lim1:
                if situation.text == 'Оберіть csv-файл':
                    situation.text = 'Графік обрано\nОберіть файл'
                elif situation.text == "Файл обрано\nОберіть вид графіка":
                    situation.text = 'Файл і графік обрано\nОберіть значення'
                X = Y = H = False
                button_x.text='Значення х'
                button_y.text = 'Значення у'
                hist_b.text="Значення"
                full_interface.remove_widget(Point_x_y)
                full_interface.add_widget(hist)
                lim = True
                lim1 = False
            elif lim and lim1:
                if situation.text == 'Оберіть csv-файл':
                    situation.text = 'Графік обрано\nОберіть файл'
                elif situation.text == "Файл обрано\nОберіть вид графіка":
                    situation.text = 'Файл і графік обрано\nОберіть значення'
                full_interface.remove_widget(Point_x_y)
                lim1 = False
########################################################################################################
        def point_press(self):
            global lim, lim1, X, Y, H
            if not lim1 and not lim:
                if situation.text == 'Оберіть csv-файл':
                    situation.text = 'Графік обрано\nОберіть файл'
                elif situation.text == "Файл обрано\nОберіть вид графіка":
                    situation.text = 'Файл і графік обрано\nОберіть значення'
                full_interface.add_widget(Point_x_y)
                lim1 = True
            elif not lim1 and lim:
                if situation.text == 'Оберіть csv-файл':
                    situation.text = 'Графік обрано\nОберіть файл'
                elif situation.text == "Файл обрано\nОберіть вид графіка":
                    situation.text = 'Файл і графік обрано\nОберіть значення'
                X = Y = H = False
                button_x.text = 'Значення х'
                button_y.text = 'Значення у'
                hist_b.text = "Значення"
                full_interface.remove_widget(hist)
                full_interface.add_widget(Point_x_y)
                lim1 = True
                lim = False
            elif lim and lim1:
                if situation.text == 'Оберіть csv-файл':
                    situation.text = 'Графік обрано\nОберіть файл'
                elif situation.text == "Файл обрано\nОберіть вид графіка":
                    situation.text = 'Файл і графік обрано\nОберіть значення'
                full_interface.remove_widget(hist)
                lim = False
#################################################################################################################
        def to_chooser(self):
            sm.current = 'choose'
#################################################################################################################
        Ch = AnchorLayout(anchor_x='left', anchor_y="top")
        def open_chooser(self, Way_to_file, MouseMotionEvent):
            global way_to_file, X, Y, H, key
            X = Y = H = False
            key = True
            way_to_file = Way_to_file
            situation.text = "Файл обрано"
            read_file()
            sm.transition = FallOutTransition()
            sm.current = 'menu'
            sm.transition = RiseInTransition()
            if '\nОберіть файл!' in situation.text: situation.text = situation.text.replace('\nОберіть файл!', '')

        Chooser = FileChooserListView(on_submit=open_chooser)
        Chooser.filters = ['*.csv']
        Ch.add_widget(Chooser)
        ChooseScreen.add_widget(Ch)
###########################################################################################
        def items_function(self):
            global X, Y, H
            if X == 1:
                X = self.text
                button_x.text = X
                situation.text = "Значення х обрано"
            elif Y == 2:
                Y = self.text
                button_y.text = Y
                situation.text = "Значення у обрано"
            if H == 3:
                H = self.text
                hist_b.text = H
                situation.text = "Будуйте графік"
            if X and X != 1 and Y and Y != 1: situation.text = "Будуйте графік"
            sm.current = 'menu'
            sm.transition = RiseInTransition()
###########################################################################################
        def func_exit_from_ItemsScreen(self):
            global X,Y,H
            if X==1:X=False
            elif Y==2:Y=False
            elif H==3:H=False
            sm.current = 'menu'
            sm.transition = RiseInTransition()
###########################################################################################
        Items = GridLayout(cols=3, rows=len_columns)
        def create_items(screen):
            global len_columns,list_of_types,columns,Items
            if screen=='items_x_y':
                try:
                    Items_X_Y_Screen.clear_widgets()
                    Items = GridLayout(cols=3, rows=len_columns)
                    exit_from_ItemsScreen = Button(text='Повернутися \nназад', background_color=[1, 0, 0, 1],on_press=func_exit_from_ItemsScreen)
                    label_for_Items = Label(text='Усі значення\nякі можна обрати:')
                    Items.add_widget(label_for_Items)
                    for i in columns:
                        if 'float' in str(list_of_types[i]) or 'int' in str(list_of_types[i]):Items.add_widget(Button(text=i, on_press=items_function))
                    Items.add_widget(exit_from_ItemsScreen)
                    Items_X_Y_Screen.add_widget(Items)
                except KeyError:
                    Items = GridLayout(cols=3, rows=len_columns)
                    exit_from_ItemsScreen = Button(text='Повернутися \nназад', background_color=[1, 0, 0, 1],
                                                   on_press=func_exit_from_ItemsScreen)
                    label_for_Items = Label(text='Усі значення\nякі можна обрати:')
                    Items.add_widget(label_for_Items)
                    for i in columns:
                        if 'float' in str(list_of_types[i]) or 'int' in str(list_of_types[i]): Items.add_widget(
                            Button(text=i, on_press=items_function))
                    Items.add_widget(exit_from_ItemsScreen)
                    Items_X_Y_Screen.add_widget(Items)
            elif screen=='items_h':
                try:
                    Items_H_Screen.clear_widgets()
                    Items = GridLayout(cols=3, rows=len_columns)
                    exit_from_ItemsScreen = Button(text='Повернутися \nназад', background_color=[1, 0, 0, 1],on_press=func_exit_from_ItemsScreen)
                    label_for_Items = Label(text='Усі значення\nякі можна обрати:')
                    Items.add_widget(label_for_Items)
                    for i in columns:Items.add_widget(Button(text=i, on_press=items_function))
                    Items.add_widget(exit_from_ItemsScreen)
                    Items_H_Screen.add_widget(Items)
                except KeyError:
                    Items = GridLayout(cols=3, rows=len_columns)
                    exit_from_ItemsScreen = Button(text='Повернутися \nназад', background_color=[1, 0, 0, 1],
                                                   on_press=func_exit_from_ItemsScreen)
                    label_for_Items = Label(text='Усі значення\nякі можна обрати:')
                    Items.add_widget(label_for_Items)
                    for i in columns: Items.add_widget(Button(text=i, on_press=items_function))
                    Items.add_widget(exit_from_ItemsScreen)
                    Items_H_Screen.add_widget(Items)
###########################################################################################
        def read_file():
            global file, key,list_of_types,len_columns,columns
            file = pd.read_csv(way_to_file[0])
            columns = file.columns.tolist()
            for i in columns:
                file[i] = pd.to_numeric(file[i], errors='ignore')
            list_of_types=file.dtypes
            len_columns = ((len(columns)) // 3)
            if len(columns) % 3 != 0: len_columns += 2
            else:len_columns+=1
#################################################################################################################
        def choose_item_item(self):
            global H,len_columns

            if len_columns!=1000:
                H=3
                create_items('items_h')
                sm.current='items_h'
                sm.transition = FallOutTransition()
            elif "\nСпершу оберіть файл" not in situation.text:situation.text+="\nСпершу оберіть файл"
#################################################################################################################
        def choose_item_x(self):
            global X,len_columns
            if len_columns!=1000:
                X=1
                create_items('items_x_y')
                sm.current='items_x_y'
                sm.transition = FallOutTransition()
            elif "\nСпершу оберіть файл" not in situation.text:situation.text+="\nСпершу оберіть файл"
#################################################################################################################
        def choose_item_y(self):
            global Y,len_columns
            if len_columns!=1000:
                Y=2
                create_items('items_x_y')
                sm.current='items_x_y'
                sm.transition = FallOutTransition()
            elif "\nСпершу оберіть файл" not in situation.text:situation.text+="\nСпершу оберіть файл"
#################################################################################################################
        def create_graphic(self):
            global file,X,Y,H,last_version_of_graphic
            if X and Y and not H:
                    data_x=file[X].tolist()
                    data_y=file[Y].tolist()
                    graphic,ax=pyplot.subplots()
                    ax.plot(data_x,data_y,'ro',color='black')
                    ax.set_xlabel(X)
                    ax.set_ylabel(Y)
                    ax.set_title(f'Залежність {Y} від {X}')
                    graphic.savefig(f'scatterplot for {X} and {Y}')
                    last_version_of_graphic=graphic
                    Picture=AnchorLayout(anchor_x='center',anchor_y='top',padding=[300,-100,50,50])
                    picture=Image(source=f'scatterplot for {X} and {Y}.png')
                    os.remove(f'scatterplot for {X} and {Y}.png')
                    Picture.add_widget(picture)
                    full_interface.add_widget(Picture)
                    situation.text='Графік побудовано'
            elif not X and not Y and H:
                data_h = file[H].tolist()

                pyplot.hist(x=data_h,color='silver',edgecolor='black')
                pyplot.xlabel(H)
                pyplot.ylabel("Кількісь")
                pyplot.title(f'Розподіл {H}')
                graphic=pyplot.figure
                pyplot.savefig(f'histogram for {H}.png')
                last_version_of_graphic = graphic
                Picture = AnchorLayout(anchor_x='right', anchor_y='top',padding=[300,-100,50,50])
                picture = Image(source=f'histogram for {H}.png')
                os.remove(f'histogram for {H}.png')
                Picture.add_widget(picture)
                full_interface.add_widget(Picture)
                pyplot.gcf().clear()
                situation.text = 'Графік побудовано'

            elif not X and not Y and not H:
                    if '\nОберіть значення!' not in situation.text: situation.text = '\nОберіть значення!'
            elif not X and Y and not H:
                    if '\nОберіть значення x!' not in situation.text: situation.text = '\nОберіть значення x!'
            elif X and not Y and not H:
                    if '\nОберіть значення y!' not in situation.text: situation.text = '\nОберіть значення y!'
            elif '\nОберіть файл!' not in situation.text:situation.text='\nОберіть файл!'
#################################################################################################################
        Create = AnchorLayout(anchor_x='left', anchor_y="bottom", padding=[25, 25, 25, 25])
        create = Button(text="Створити", size_hint=[0.3, 0.2])
        Create.add_widget(create)
        Create = AnchorLayout(anchor_x='left', anchor_y="bottom", padding=[25, 25, 25, 25])
        Choose = BoxLayout(orientation='vertical', spacing='5', size_hint=[0.3, 0.2])
        choose = Button(text='Обрати файл', background_color=[0, 0.8, 0.8, 1], on_press=to_chooser)
        create = Button(text="Побудувати", background_color=[0.8, 0.8, 0, 1],on_press=create_graphic)
        Choose.add_widget(choose)
        Choose.add_widget(create)
        Create.add_widget(Choose)

        Save = AnchorLayout(anchor_x='center', anchor_y="bottom", padding=[25, 25, 25, 25])
        save = Button(text='Зберегти', size_hint=[0.3, 0.2])
        Save.add_widget(save)
        Save = AnchorLayout(anchor_x='center', anchor_y="bottom", padding=[25, 25, 25, 25])
        Choose2 = BoxLayout(orientation='vertical', spacing='5', size_hint=[0.3, 0.2])
        save = Button(text='Зберегти', background_color=[0, 1, 0, 1])
        new = Button(text="Новий", background_color=[0.8, 0.8, 0, 1])
        Choose2.add_widget(save)
        Choose2.add_widget(new)
        Save.add_widget(Choose2)

        Exit = AnchorLayout(anchor_x='right', anchor_y="bottom", padding=[25, 25, 25, 25])
        exit = Button(text='Вийти', size_hint=[0.3, 0.2], background_color=[1, 0, 0, 1])
        Exit.add_widget(exit)

        Situation = AnchorLayout(anchor_x='right', anchor_y="top", padding=[25, 25, 25, 25])
        situation=Label(text='Оберіть csv-файл')
        #Situation.add_widget(situation)

        full_interface = RelativeLayout()
        full_interface.add_widget(Create)
        full_interface.add_widget(Save)
        full_interface.add_widget(Exit)
        full_interface.add_widget(Situation)

        dropdown = DropDown()

        hist = AnchorLayout(anchor_x='left', anchor_y="center", padding=[25, 25, 25, 25])
        hist_b = Button(text='Значення', size_hint=[0.3, 0.2],on_press=choose_item_item)
        hist.add_widget(hist_b)

        histogram = Button(text='Гістограма', size_hint_y=None, height=70, background_color=[0.2, 0.8, 0.6, 1])
        histogram.bind(on_release=lambda histogram: dropdown.select(histogram.text), on_press=hist_press)
        dropdown.add_widget(histogram)

        Point_x_y = AnchorLayout(anchor_x='left', anchor_y="center", padding=[25, 25, 25, 25])
        point_x_y = BoxLayout(orientation='vertical', spacing='5', size_hint=[0.3, 0.2])
        button_x = Button(text='Значення x',on_press=choose_item_x)
        button_y = Button(text='Значення y',on_press=choose_item_y)
        point_x_y.add_widget(button_x)
        point_x_y.add_widget(button_y)
        Point_x_y.add_widget(point_x_y)

        points = Button(text='Точковий', size_hint_y=None, height=70, background_color=[0.2, 0.8, 0.6, 1])
        points.bind(on_release=lambda points: dropdown.select(points.text), on_press=point_press)
        dropdown.add_widget(points)

        mainbutton = Button(text='Вид графіка')
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))


        Type_of_graphic = AnchorLayout(anchor_x='left', anchor_y="top", padding=[25, 25, 25, 25])
        Hist_with_situation=BoxLayout(orientation='vertical',spacing='5', size_hint=[0.3, 0.2])
        Hist_with_situation.add_widget(situation)
        Hist_with_situation.add_widget(mainbutton)
        Type_of_graphic.add_widget(Hist_with_situation)

        full_interface.add_widget(Type_of_graphic)
        MenuScreen.add_widget(full_interface)
        ###########################################################################################
        sm.current = 'menu'
        return sm
if __name__ == '__main__':
    cursachApp().run()
#python 1_kivy.py