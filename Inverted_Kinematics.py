import numpy

def reposition(next_x, next_y, arm_1_x, arm_1_y, arm_1_angle,
                arm_2_x, arm_2_y, arm_2_angle, arm_3_x, arm_3_y, arm_3_angle,
                arm_4_x, arm_4_y, arm_4_angle, arm_5_x, arm_5_y, arm_5_angle,
                arm_6_x, arm_6_y, arm_6_angle, arm_7_x, arm_7_y, arm_7_angle):
    ##Function optimizes for least amount of arm movement to get to desired point
    print("Repositioning...")




def main():
    ##Basic Inverted Kinematics Script that will recalculate the current arm position in order to get to desired point
    ##For a 7 axis Robotic Arm

    #Opens Arm dimensions JSON to get the current arm dimensions
    ifile = open('arm_dimensions', "r")
    parameters = json.load(ifile)

    #Input the desired coordinates in order to reposition
    next_x, next_y = input("Input Desired Coordinates (X, Y): ")
    reposition(next_x, next_y)

    #Current Coordinates (Current Coordinates is referring to end of arm, beginning of arm is end of last arm or base)
    arm_1_x, arm_1_y, arm_1_angle = parameters["arm_1"].curr_x, parameters["arm_1"].curr_y, parameters["arm_1"].angle
    arm_2_x, arm_2_y, arm_2_angle = parameters["arm_2"].curr_x, parameters["arm_2"].curr_y, parameters["arm_1"].angle
    arm_3_x, arm_3_y, arm_3_angle = parameters["arm_3"].curr_x, parameters["arm_3"].curr_y, parameters["arm_1"].angle
    arm_4_x, arm_4_y, arm_4_angle = parameters["arm_4"].curr_x, parameters["arm_4"].curr_y, parameters["arm_1"].angle
    arm_5_x, arm_5_y, arm_5_angle = parameters["arm_5"].curr_x, parameters["arm_5"].curr_y, parameters["arm_1"].angle
    arm_6_x, arm_6_y, arm_6_angle = parameters["arm_6"].curr_x, parameters["arm_6"].curr_y, parameters["arm_1"].angle
    arm_7_x, arm_7_y, arm_7_angle = parameters["arm_7"].curr_x, parameters["arm_7"].curr_y, parameters["arm_1"].angle

main()