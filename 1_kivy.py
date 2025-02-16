from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

Config.set("graphics","resiziable",'0')
Config.set("graphics","width",'640')
Config.set("graphics","height",'480')

lim=False
lim1=False

class cursachApp(App):
    def build(self):


        def hist_press(self):
            global lim
            global lim1
            if not lim and not lim1:
                full_interface.add_widget(hist)
                lim=True
            elif not lim and lim1:
                full_interface.remove_widget(Point_x_y)
                full_interface.add_widget(hist)
                lim=True
                lim1=False
            elif lim and lim1:
                full_interface.remove_widget(Point_x_y)
                lim1=False

        def point_press(self):
            global lim1
            global lim
            if not lim1 and not lim:
                full_interface.add_widget(Point_x_y)
                lim1=True
            elif not lim1 and lim:
                full_interface.remove_widget(hist)
                full_interface.add_widget(Point_x_y)
                lim1=True
                lim=False
            elif lim and lim1:
                full_interface.remove_widget(hist)
                lim=False



        Create = AnchorLayout(anchor_x='left', anchor_y="bottom", padding=[25, 25, 25, 25])
        create = Button(text="Створити", size_hint=[0.3, 0.2])
        Create.add_widget(create)
        Create = AnchorLayout(anchor_x='left', anchor_y="bottom", padding=[25, 25, 25, 25])
        Choose = BoxLayout(orientation='vertical', spacing='5', size_hint=[0.3, 0.2])
        choose = Button(text='Обрати файл',background_color=[0,0.8,0.8,1])
        create = Button(text="Створити",background_color=[0.8,0.8,0,1])
        Choose.add_widget(choose)
        Choose.add_widget(create)
        Create.add_widget(Choose)

        Save = AnchorLayout(anchor_x='center', anchor_y="bottom",padding=[25,25,25,25])
        save = Button(text='Зберегти',size_hint=[0.3,0.2])
        Save.add_widget(save)
        Save = AnchorLayout(anchor_x='center', anchor_y="bottom", padding=[25, 25, 25, 25])
        Choose2 = BoxLayout(orientation='vertical', spacing='5', size_hint=[0.3, 0.2])
        save = Button(text='Зберегти',background_color=[0,1,0,1])
        new = Button(text="Новий",background_color=[0.8,0.8,0,1])
        Choose2.add_widget(save)
        Choose2.add_widget(new)
        Save.add_widget(Choose2)

        Exit = AnchorLayout(anchor_x='right', anchor_y="bottom",padding=[25,25,25,25])
        exit = Button(text='Вийти', size_hint=[0.3, 0.2],background_color=[1,0,0,1])
        Exit.add_widget(exit)

        full_interface=FloatLayout(size=(480,640))
        full_interface.add_widget(Create)
        full_interface.add_widget(Save)
        full_interface.add_widget(Exit)

        dropdown=DropDown()

        hist=AnchorLayout(anchor_x='left', anchor_y="center", padding=[25,25,25,25])
        hist_b=Button(text='Значення', size_hint=[0.3,0.2])
        hist.add_widget(hist_b)

        histogram=Button(text='Гістограма',size_hint_y=None, height=70,background_color=[0.2,0.8,0.6,1])
        histogram.bind(on_release=lambda histogram: dropdown.select(histogram.text),on_press= hist_press)
        dropdown.add_widget(histogram)



        Point_x_y=AnchorLayout(anchor_x='left', anchor_y="center", padding=[25,25,25,25])
        point_x_y=BoxLayout(orientation='vertical',spacing='5',size_hint=[0.3,0.2])
        button_x=Button(text='Значення x')
        button_y=Button(text='Значення y')
        point_x_y.add_widget(button_x)
        point_x_y.add_widget(button_y)
        Point_x_y.add_widget(point_x_y)



        points = Button(text='Точковий',size_hint_y=None, height=70,background_color=[0.2,0.8,0.6,1])
        points.bind(on_release=lambda points: dropdown.select(points.text), on_press=point_press)
        dropdown.add_widget(points)

        mainbutton = Button(text='Вид графіка', size_hint=[0.3,0.2])
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

        Type_of_graphic=AnchorLayout(anchor_x='left', anchor_y="top",padding=[25,25,25,25])
        Type_of_graphic.add_widget(mainbutton)
        full_interface.add_widget(Type_of_graphic)

        return full_interface


if __name__ == '__main__':
    cursachApp().run()
#python kivy_venv\1_kivy.py
