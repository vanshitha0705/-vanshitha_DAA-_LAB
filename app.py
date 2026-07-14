import gradio as gr

def run_experiment(exp_name):
    if exp_name == "Experiment 1":
        return " Executing Experiment 1 Logic...\n(Your DAA Analysis Output will appear here)"
    elif exp_name == "Experiment 2":
        return " Executing Experiment 2 Logic...\n(Your DAA Analysis Output will appear here)"
    elif exp_name == "Experiment 3":
        return " Executing Experiment 3 Logic...\n(Your DAA Analysis Output will appear here)"
    elif exp_name == "Experiment 4":
        return " Executing Experiment 4 Logic...\n(Your DAA Analysis Output will appear here)"
    return "Please select an experiment."

# Define the user interface layout
with gr.Blocks(title="DAA Lab UI") as demo:
    gr.Markdown("#  Design & Analysis of Algorithms Lab")
    gr.Markdown("Select an experiment from the dropdown menu to check its analysis and output.")
    
    with gr.Row():
        vocab_dropdown = gr.Dropdown(
            choices=["Experiment 1", "Experiment 2", "Experiment 3", "Experiment 4"], 
            label="Choose DAA Experiment",
            value="Experiment 1"
        )
    
    output_text = gr.Textbox(label="Execution Output", lines=10)
    
    # Trigger application logic when the dropdown selection changes
    vocab_dropdown.change(fn=run_experiment, inputs=vocab_dropdown, outputs=output_text)

demo.launch()
