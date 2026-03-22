# 🔢 NumPy Learning Journey

My personal notes and practice files for learning **NumPy** — from basics to array operations and problem solving!

---

## 📚 What I Learned

### 📘 Introduction — `Introduction.ipynb`
- Array creation functions — `np.arange()`, `np.zeros()`, `np.ones()`, `np.linspace()`, `np.array()`
- Array attributes — `.shape`, `.size`, `.dtype`
- Useful methods — `.min()`, `.max()`, `.mean()`, `.std()`, `.sum()`, `.argmin()`, `.argmax()`, `.reshape()`, `.resize()`

### 📗 Indexing — `numpy_indexing.ipynb`
- 1D & 2D array indexing
- Slicing — `arr[0:3]`, `arr[:, 1]`
- Row & column access — `arr[1][2]`, `arr[:, 1]`

### 📙 Advance Indexing — `advance-indexing.ipynb`
- **2D Matrix Indexing** — `mat[[0,1,3],[0,1,4]]` → Specify both row and column — like giving an exact seat number to get that student's record! 🎯
- **Conditional Selection** — `arr[arr>20]` → "Show me only students who scored more than 20!" Apply a condition, get filtered data instantly! ✅
- **np.where()** — Does three things:
  - `np.where(arr>20)` → Tells you the index position — "who all passed?" 
  - `np.where(arr>20, arr, 0)` → Condition true → keep the value, false → replace with 0! Like "keep marks of those who passed, make it 0 for those who failed!" 💡

### 📕 Array Operations — `array_operations.ipynb`
- Addition, Subtraction, Multiply, Division
- Matrix operations — Power, Floor Division, Modulus
- Works on both **1D and 2D matrices!**

### 📓 Problem Solving — `numpy_problem-solving.ipynb`
- ✅ Average age of students
- ✅ Highest science marks
- ✅ Students who scored more than 90 in Maths
- ✅ Increase Maths marks of all students by 5
- ✅ Students younger than 19
- ✅ Column-wise average marks (axis=0)
- ✅ Students scoring at least 80 in two subjects
- ✅ Replace Science marks below 75 with 0

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## 📂 Project Structure

```
numpy-learning/
│── Introduction.ipynb
│── numpy_indexing.ipynb
│── adance-indexing.ipynb
│── array_operations.ipynb
│── numpy_problem-solving.ipynb
```

---

## 🎯 What I Learned

- NumPy array creation & attributes
- Indexing, slicing & advance indexing techniques
- Conditional selection & np.where()
- Mathematical operations on arrays
- Solving real-world data problems with NumPy

---

## 👩‍💻 Author

**Monika Gupta**


[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/monika-gupta-9ab3a6335)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:monika8920193@gmail.com)

---

> ⭐ *Learning NumPy one array at a time!*
