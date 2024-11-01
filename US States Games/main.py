from turtle import  Screen
import pandas as pd
from state import State
from informations import Info


screen=Screen()
info=Info()

screen.setup(width=725,height=491)
screen.bgpic('blank_states_img.gif')
screen.title('Name the States')

df=pd.read_csv('50_states.csv')
guessed_states_number=0
guessed_states_list=[]


while guessed_states_number !=50:
    states_list=df['state'].to_list()
    title=f"{guessed_states_number}/{len(states_list)} States Correct"
    user_input=screen.textinput(title,"What's another state name?: ").title()
    if user_input=="Exit":
        break
    if user_input  not in states_list:
        info.no_state()
    elif user_input  in guessed_states_list:
        info.already_exist()
    elif user_input  in states_list:
        chosen_state=df[df['state']==user_input]
        x=chosen_state['x'].iloc[0]
        y=chosen_state['y'].iloc[0]
        state=State(user_input,x,y)
        guessed_states_number+=1
        guessed_states_list.append(user_input)

if guessed_states_number==50:
    info.win()

states_to_learn=[]

for item in states_list:
    if item not in guessed_states_list:
        states_to_learn.append(item)

data_dict={"States to learn": states_to_learn}

df_states_to_learn=pd.DataFrame(data_dict)
df_states_to_learn.index=df_states_to_learn.index+1
df_states_to_learn.to_csv("states_to_learn.csv")








