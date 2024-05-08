import streamlit as st 
def main():
    st.title("input ex")
    ti=st.text_input("enter ur name")
    st.write(f" you entred :  {ti} ")
    ni=st.number_input(" enter age")
    st.write(f"entered : {ni}")
    in_checkbox=st.checkbox("CSE")
    input_second_checkbox=st.checkbox("E E")
    if(in_checkbox ==True and input_second_checkbox==True):
        st.write("both r checked")
    elif(in_checkbox == True or input_second_checkbox==True):
        st.write("only one checkbox is checked")
    elif(in_checkbox == True and input_second_checkbox==False):
        st.write("only one checkbox is checked first")  
    elif(in_checkbox == False and input_second_checkbox==True):
        st.write("only one checkbox is checked second ")   
    else :
        st.write(" none checked")       
    h=["cse","ece"]
    w=st.radio(" your seelected department is" , h)
    st.write(w)
    input_dropdown =st.selectbox("section" , ('1','2','3','4'))
    st.write(input_dropdown)
    drop2=st.multiselect("select hobbies",['singing','reading','crafting'])
    st.write('country selected:',drop2)
    slider1=st.slider("choose value :",min_value=0,max_value=100,value=50)
    st.write('u have selected:',slider1)

if __name__=="__main__":
    main()    