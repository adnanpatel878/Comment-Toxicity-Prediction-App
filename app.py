import streamlit as st
import altair as alt
import pandas as pd
import pickle

# Load the TF-IDF vocabulary specific to the category
# (Assuming the rest of the code remains the same)

# Streamlit app
def main():
    st.title("Toxicity Prediction App")

    # Input text box for user input
    user_input = st.text_area("Enter Comment:")

    # Initialize prediction results variables
    out_tox, out_sev, out_obs, out_ins, out_thr, out_ide = 0, 0, 0, 0, 0, 0

    # Predict button
    if st.button("Predict"):
        if user_input:
            data = [user_input]

            # Rest of the prediction code

            out_tox = round(pred_tox[0], 2)
            out_sev = round(pred_sev[0], 2)
            out_obs = round(pred_obs[0], 2)
            out_ins = round(pred_ins[0], 2)
            out_thr = round(pred_thr[0], 2)
            out_ide = round(pred_ide[0], 2)

            st.write("Prob (Toxic):", out_tox)
            st.write("Prob (Severe Toxic):", out_sev)
            st.write("Prob (Obscene):", out_obs)
            st.write("Prob (Insult):", out_ins)
            st.write("Prob (Threat):", out_thr)
            st.write("Prob (Identity Hate):", out_ide)

            # Bar chart using altair
            categories = ['Toxic', 'Severe Toxic', 'Obscene', 'Insult', 'Threat', 'Identity Hate']
            percentages = [out_tox, out_sev, out_obs, out_ins, out_thr, out_ide]

            data_chart = pd.DataFrame({'Category': categories, 'Percentage': percentages})
            chart = alt.Chart(data_chart).mark_bar().encode(
                x='Category:N',
                y='Percentage:Q',
                tooltip=['Category', 'Percentage']
            ).properties(
                width=400
            )

            st.altair_chart(chart, use_container_width=True)

        else:
            st.warning("Please enter some text.")

    # Footer with specific padding from the bottom
    footer_html = """
    <style>
        .footer {
            position: fixed;
            bottom: 1cm;
            width: 100%;
            text-align: center;
        }
    </style>
    <div class="footer">
        <p><a href="https://www.linkedin.com/in/adnan-patel-b78ba521b/" target="_blank">Connect with me on LinkedIn @adnanpatel</a></p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
