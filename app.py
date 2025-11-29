import gradio as gr

def bubble_sort_steps(arr):
    steps = []
    n = len(arr)
    if n <= 1:
        steps.append(f"No sorting needed for list of length {n}.")
        return steps
    pass_num = 0
    while True:
        swapped = False
        for i in range(0, n - 1 - pass_num):
            a, b = arr[i], arr[i+1]
            if a > b:
                arr[i], arr[i+1] = b, a
                swapped = True
                steps.append(f"Comparing {a} and {b}: swapped -> {arr}")
            else:
                steps.append(f"Comparing {a} and {b}: no swap -> {arr}")
        pass_num += 1
        if not swapped:
            steps.append("No swaps in this pass, the list is sorted.")
            break
        if pass_num >= n - 1:
            break
    return steps

def simulate_bubble_sort(input_str):
    if not input_str or input_str.strip() == "":
        return "Please enter a comma-separated list of integers like: 1, 2, 3"

    parts = input_str.strip().split(",")

    arr = []
    for part in parts:
        part = part.strip()
        if not part or not part.lstrip("-").isdigit():
            return "Invalid input. Please enter integers only, separated by commas like: 4, 10, -2, 0"
        arr.append(int(part))

    steps = bubble_sort_steps(arr)
    output_lines = [f"{idx+1}. {step}" for idx, step in enumerate(steps)]
    return "\n".join(output_lines)

demo = gr.Interface(
    fn=simulate_bubble_sort,
    inputs=gr.Textbox(label="Enter numbers to sort", placeholder="e.g. 5, 2, 9, 1"),
    outputs=gr.Markdown(label="Bubble Sort Steps"),
    title="Bubble Sort Simulator",
    description="Enter a list of integers (comma or space separated) and follow the sorting steps."
)

demo.examples = [["5, 2, 9, 1"]]

if __name__ == "__main__":
    demo.launch()
