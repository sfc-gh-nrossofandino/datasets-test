import streamlit as st

conn = st.connection("snowflake")
conn.cursor().execute('use database FREE_DATASET_GZTSZAS2KH9')
query = conn.query("""SELECT i.cik, i.company_name, r.period_start_date, r.period_end_date, r.measure_description, TO_NUMERIC(r.value) AS value
FROM cybersyn.sec_cik_index AS i
JOIN cybersyn.sec_report_attributes AS r ON (r.cik = i.cik)
WHERE i.sic_code_description = 'AIR TRANSPORTATION, SCHEDULED'
  AND r.statement = 'Income Statement'
  AND r.period_end_date = '2022-12-31'
  AND r.covered_qtrs = 4
  AND r.metadata IS NULL
  AND r.measure_description IN ('Total operating revenues', 'Total operating revenue');""")
st.dataframe(query)