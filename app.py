import gradio as gr

def generate(text, category, language):
    if category == "Essay":
        return f"Here is an essay in {language} on the topic: {text}"
    elif category == "Poem":
        return f"This is a poem in {language} on: {text}"
    elif category == "Muktak":
        return f"Muktak:\n{text} ({language})"
    elif category == "Shayari":
        return f"Shayari:\n{text} ({language})"
    else:
        return "Invalid Category."

iface = gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(label="Topic or Theme"),
        gr.Dropdown(["Essay", "Poem", "Muktak", "Shayari"], label="Category"),
        gr.Radio(["Nepali", "English"], label="Language")
    ],
    outputs="text",
    title="✍️ Radhika Ma Vi - Student AI",
    description="AI for generating Essay, Poem, Muktak, Shayari in Nepali & English."
)

iface.launch()
