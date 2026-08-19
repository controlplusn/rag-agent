from retrieval_chain import chain

def main():
    print("RAG Chat")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("User: ")

        if question.lower() == "exit":
            break

        response = chain.invoke(question)

        print(f"\nAI: {response}\n")


if __name__ == "__main__":
    main()