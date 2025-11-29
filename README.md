---
title: Bubble Sort
emoji: 🌖
colorFrom: indigo
colorTo: gray
sdk: gradio
sdk_version: 6.0.1
app_file: app.py
pinned: false
---

# Bubble Sort
## Demo video/gif/screenshot of test

## Problem Breakdown & Computational Thinking

i choose **Bubble Sort** becuase it is simple. it is easy to explain and see what happens. in class we learn it early so it makes sense to use.

we think step by step before making the code. this is called computational thinking.

**Decomposition:** i break down bubble sort into many steps. it compare two numbers, then maybe swap them. then again and again. this repeat until all done.

**Pattern Recognition:** each time biggest number go to the end. then next biggest. it happens same way every time. we can see this pattern.

**Abstraction:** we only show what user need. comparisons and swaps. we don’t show boring stuff like index i and j or variables inside loop.

**Algorithm Design:** user type some numbers. then click button. the app show how numbers got sorted. we use Gradio to make it simple. it easy to use and looks clean.

## Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Get Input from User]
    B --> C[Validate Input]
    C -->|Invalid| D[Show Error Message]
    C -->|Valid| E[Run Bubble Sort]
    E --> F[Compare two items]
    F --> G{Is first > second?}
    G -->|Yes| H[Swap them]
    G -->|No| I[No swap]
    H --> J[Record step]
    I --> J
    J --> K{More items to compare in pass?}
    K -->|Yes| F
    K -->|No| L[Check if swapped happened]
    L -->|Yes| E
    L -->|No| M[Done Sorting]
    M --> N[Show steps to user]
    N --> O[End]

## Steps to Run
1. **Clone or Download** this project repository to your local machine. Make sure you have Python 3 installed.
2. **Install Dependencies:** In a terminal, navigate to the project folder and run `pip install -r requirements.txt`. This will install Gradio (the UI library).
3. **Run the Application:** Execute `python app.py`. This will launch the Gradio app on a local web server (it will display a local URL, usually http://localhost:7860).
4. **Open the Interface:** If it doesn’t open automatically, copy the localhost link into your web browser. You should see the Bubble Sort Simulator UI.
5. **Use the App:** Enter a list of integers (separated by commas or spaces) into the input box, then press the submit button. You will see the sorting steps appear, one by one, showing how the algorithm sorted your list.  
*(Alternatively, as it's deployed on Hugging Face, you could run it in the browser without any installation.)*

## Hugging Face Link
The app will be deployed on Hugging Face Spaces. Link to the live demo: _(coming soon)_.

## Author & Acknowledgment
**Author:** Mohammad Rajin Sharwar
**Acknowledgment:** Thanks to the CISC-121 course instructors for their guidance and tips. Also, the VisuAlgo site was a great reference for understanding and explaining bubble sort behavior.