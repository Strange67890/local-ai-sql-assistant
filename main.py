from langchain_community.utilities import SQLDatabase
from langchain_ollama import ChatOllama
from urllib.parse import quote_plus

# ==========================================
# 1. DATABASE CONNECTION
# ==========================================
db_user = "root"
raw_password = "Frank@2004"
db_password = quote_plus(raw_password)
db_host = "localhost"
db_name = "manpower_ai_db"

try:
    db = SQLDatabase.from_uri(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:3306/{db_name}")
    print("✅ Database Connected Successfully!")
except Exception as e:
    print(f"❌ Connection Failed: {e}")
    exit()

# ==========================================
# 2. INITIALIZE OLLAMA
# ==========================================
llm = ChatOllama(model="phi3", temperature=0)

# ==========================================
# 3. THE "NO-LOOP" LOGIC
# ==========================================
def ask_database(question):
    print(f"\nThinking about: '{question}'...")
    
    # Step A: Get the table info so the AI knows what to write
    schema = db.get_table_info()
    
    # Step B: Create a strict prompt for SQL generation
    prompt = f"""
    You are a MySQL expert. 
    Here is the database schema:
    {schema}
    
    Write a SQL query to answer this question: "{question}"
    
    IMPORTANT RULES:
    1. Return ONLY the SQL query. 
    2. Do not explain your thought process.
    3. Do not use Markdown or backticks (```).
    4. Start the query immediately with SELECT.
    """

    # Step C: Get SQL from AI
    response = llm.invoke(prompt)
    sql_query = response.content.strip()
    
    # Clean up if the AI accidentally added markdown code blocks
    sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
    
    print(f"📝 Generated SQL: {sql_query}")

    # Step D: Run the SQL on the real database
    try:
        result = db.run(sql_query)
        return result
    except Exception as e:
        return f"Error executing SQL: {e}"

# ==========================================
# 4. CHAT LOOP
# ==========================================
if __name__ == "__main__":
    print("\n--------------------------------------------------")
    print("🤖 STABLE SQL ASSISTANT IS READY")
    print("--------------------------------------------------\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        answer = ask_database(user_input)
        print(f"💡 Answer: {answer}\n")