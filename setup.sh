mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"vigneshedithal11031997v@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
