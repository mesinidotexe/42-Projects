*This project has been created as part of the 42 curriculum by <vmesini->.*

# push_swap

## Description

**push_swap** is a sorting algorithm project from the 42 curriculum.  
The goal is to sort a stack of integers using a **limited set of operations** and the **smallest possible number of moves**.

The program receives a list of integers as arguments and must output a sequence of instructions that sorts the numbers in ascending order using two stacks:

- **Stack A** (initial stack)
- **Stack B** (auxiliary stack)

Only the following operations are allowed:

- `sa`, `sb`, `ss`
- `pa`, `pb`
- `ra`, `rb`, `rr`
- `rra`, `rrb`, `rrr`

The main challenge is **algorithm efficiency**, especially for larger inputs (100 and 500 numbers), where the number of operations must remain under specific limits.

### Project Goals

- Implement stack manipulation from scratch.
- Work with linked lists or similar data structures.
- Optimize sorting logic for different input sizes.
- Develop algorithmic thinking (e.g., small sort strategies and radix sort for larger sets).

---

## Features

- Custom stack implementation
- Optimized sorting for:
  - 2–3 numbers (minimal moves)
  - 4–5 numbers (small-sort strategy)
  - Larger inputs using **Radix Sort (bitwise approach)**
- Error handling:
  - Non-numeric arguments
  - Duplicates
  - Integer overflow
- Memory management without leaks

---

## How It Works

### Small Inputs (≤ 5 numbers)

For small stacks, hardcoded logical strategies are used to guarantee the minimum number of moves.

### Larger Inputs (> 5 numbers)

For larger datasets, a **binary Radix Sort** approach is used:

1. Normalize the numbers (index them from smallest to largest).
2. Sort numbers bit by bit (starting from the least significant bit).
3. Use `pb` and `ra` depending on the current bit.
4. Move elements back from stack B to stack A after each bit pass.

This ensures efficient sorting within the movement limits required by the project.

---

## Instructions

### Compilation

```bash
make
```

This will build the `push_swap` executable (and the `libft` dependency if needed).

### Execution

```bash
./push_swap <numbers>
```

Pass a list of integers as arguments. The program will output a sequence of operations that sorts them in ascending order.

**Examples:**

```bash
./push_swap 2 1 3
./push_swap 4 2 5 1 3
```

**Test with random input (100 numbers):**

```bash
var=$(seq 0 99 | shuf) && ./push_swap $var
```

---

## Resources

### References

- [42 push_swap Subject](https://cdn.intra.42.fr/pdf/pdf/96035/en.subject.pdf) — Official project PDF
- [Radix Sort (Wikipedia)](https://en.wikipedia.org/wiki/Radix_sort) — Bitwise radix sort for stack-based sorting
- [Sorting algorithms](https://en.wikipedia.org/wiki/Sorting_algorithm) — General overview of sorting strategies
- [42 push_swap Guide](https://medium.com/@jamierobertdawson/push-swap-the-least-amount-of-moves-with-two-stacks-d1e76a71789a) — Tutorial on optimization strategies

### AI Usage

AI was used to help find possible ways and logics throughout the program, inplement fuctions, code review, understanding the use of Radix sorting algorithm and writing this README
