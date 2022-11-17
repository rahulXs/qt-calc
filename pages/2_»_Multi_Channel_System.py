import math

import streamlit as st
from utils import add_logo

st.set_page_config(
    page_title="CQC - MCS",
    page_icon="img/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


add_logo()

with st.sidebar:
    st.write("\n\n")
    st.caption("Multi Channel System, M/M/S")
    st.sidebar.info(
        "Multi server queue has two or more service facility in parallel providing identical service."
    )

st.caption("Queuing theory calculator")
st.markdown("### Model B: Multi Channel System, M/M/S")

lambda_val = st.number_input(
    "Enter mean number of arrivals per time period (λ) : ",
    value=1.0,
    step=1.0,
    format="%.2f",
)
mu_val = st.number_input(
    "Enter mean number of people or items served per time period (μ) : ",
    value=2.0,
    step=1.0,
    format="%.2f",
)
m = st.number_input(
    "Enter number of channels open (M) : ", value=2, min_value=2, step=1
)

check = st.button("Calculate")
if check:
    # Calculations
    prod_m_mu = m * mu_val
    div_lambda_mu = lambda_val / mu_val

    if prod_m_mu <= lambda_val:
        st.error("Incorrect Input: Please, try again.")
        st.warning(
            "Hint: For Probability (p0) calculation, the value of M*μ should be greater than λ"
        )
    else:
        # calculate p0
        p0 = None

        exp1 = prod_m_mu / (prod_m_mu - lambda_val)
        exp2 = 1 / (math.factorial(m))
        exp3 = (lambda_val / mu_val) ** m
        exp123 = exp1 * exp2 * exp3

        sigma = 0
        for n in range(0, m):
            sigma += (1 / math.factorial(n)) * ((lambda_val / mu_val) ** n)

        if m * mu_val > lambda_val:
            p0 = 1 / (sigma + exp123)

        # calculate ls
        exp4 = (lambda_val * mu_val) * (div_lambda_mu**m)
        exp5 = math.factorial(m - 1) * ((prod_m_mu - lambda_val) ** 2)

        ls = (exp4 / exp5) * p0 + div_lambda_mu

        # calculate ws, lq, wq
        ws = ls / lambda_val
        lq = ls - div_lambda_mu
        wq = lq / lambda_val

        st.info("Output: Multi Channel System, M/M/S")

        out_str = f"""
    Probability that there are zero people or units in the system (p0):         {round(p0, 4)}
Average number of people or units in the system (Ls):                       {round(ls, 4)}
Average time a unit spends in the waiting line and being serviced (Ws):     {round(ws, 4)}
Average number of people or units in line waiting for service (Lq):         {round(lq, 4)}
Average time a person or unit spends in the queue waiting for service (Wq): {round(wq, 4)}"""
        st.code(out_str)

        with st.expander("See explanation"):
            st.write(
                "The following Queuing theory *formulas* for *Multi Channel System (M/M/S)* were used for calculations:"
            )
            st.latex(
                r"""
                \textup{Number of channels open:} \;  M
                """
            )
            st.latex(
                r"""
                \textup{Average arrival rate:} \;  \lambda
                """
            )
            st.latex(
                r"""
                \textup{Average service rate at each channel:} \;  \mu
                """
            )
            st.latex(
                r"""
                \textup{Probability that there are zero people or units in the system:} \; P_{0} = \frac{1}{\left [ \sum_{n=0}^{M-1} \frac{1}{n!} \left ( \frac{\lambda}{\mu}\right )^n\right ] + \frac{1}{M!} \left ( \frac{\lambda}{\mu} \right )^M \frac{M\mu}{M\mu - \lambda}}  \; \; \textup{for} \; M\mu > \lambda
                """
            )
            st.latex(
                r"""
                \textup{Average number of people or units in the system:} \; L_{S} = \frac{\lambda\mu \left (\frac{\lambda}{\mu}  \right )^M}{\left ( M-1 \right )! \left ( M\mu - \lambda \right )^{2}} P_{0} + \frac{\lambda}{\mu}
                """
            )
            st.latex(
                r"""
                \textup{Average time a unit spends in the waiting line and being serviced:} \; W_{S} = \frac{\mu \left (\frac{\lambda}{\mu}  \right )^M}{\left ( M-1 \right )! \left ( M\mu - \lambda \right )^{2}} P_{0} + \frac{1}{\mu} = \frac{L_{S}}{\lambda}
                """
            )
            st.latex(
                r"""
                \textup{Average number of people or units in line waiting for service:} \; L_{q} = L_{S} - \frac{\lambda}{\mu}
                """
            )
            st.latex(
                r"""
                \textup{Average time a person or unit spends in the queue waiting for service:} \; W_{q} = W_{S} - \frac{1}{\mu} = \frac{L_{q}}{\lambda}
                """
            )
