import turtle
from turtle import Turtle, Screen

import pandas

screen = Screen()
tt= Turtle()
state_write_turtle = Turtle()
screen.title('US State Game')
image = 'blank_states_img.gif'
screen.addshape(image)

tt.shape(image)
state_write_turtle.up()
state_write_turtle.ht()

data =pandas.read_csv('50_states.csv')
current_score = 0

states = data.state.tolist()
guessed_states = []
#missed_states= []
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# dict_rows = {row[0]: tuple(row[1:]) for row in data.itertuples(index = False, name = None)}

# print(dict_rows)
# print(dict_rows['Alabama'])
#
x_values = data['x'].to_list()
y_values = data['y'].to_list()
joint_values = list(zip(x_values, y_values))
state_and_points_dict = dict(zip(states, joint_values))

print(state_and_points_dict)



while current_score < 50:
    answer_state = screen.textinput(title= f"{current_score}/50 States Correct",
                                    prompt= 'State name' ).title()
    if answer_state == 'Exit':
        print(guessed_states)
        print('You missed the following states:')

        missed_states = [state for state in states if state not in guessed_states]
        print (missed_states)

        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('state_to_learn.csv')

        break

    if answer_state in state_and_points_dict:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            state_write_turtle.goto(state_and_points_dict[answer_state])
            state_write_turtle.write(answer_state)
            #print(guessed_states)
            current_score+=1

# State not guessed

#if current_score < 50:
#     print('You missed the following states:')
#     for state in states:
#         if state not in guessed_states:
#             print(state)
#             missed_states.append(state)
#
#
# new_data = pandas.DataFrame(missed_states)
# new_data.to_csv('state_to_learn.csv')

#print(missed_states)

#screen.mainloop()