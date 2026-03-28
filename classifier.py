import streamlit as st
from openai import OpenAI
import os

client = OpenAI() # OpenAI client

st.title("DDC Concept Classifier")

concept = st.text_input("Enter a concept") # 사용자 입력

if st.button("Classify"): # 버튼 클릭
	if concept:
		prompt = f"""
			What is the most appropriate Dewey Decimal Classification (DDC) number for the concept: {concept}

			Return:
			DDC number
			short explanation
			"""

		# OpenAI API 호출 -> 이때 credit 감소
		response = client.responses.create(
		model="gpt-5-mini",
		input=prompt
		)

		result = response.output_text # 결과 추출

		st.subheader("Result") # 화면 출력
		st.write(result)
