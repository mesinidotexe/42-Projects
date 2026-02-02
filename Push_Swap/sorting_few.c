#include "push_swap.h"

static void	sorting_three(t_stack *a)
{
	int	first;
	int	second;
	int	third;
	
	first = a->number;
	second = a->next->number;
	third = a->next->next->number;
	if (first > second && second > third) // 3 2 1
	{
		ra(a);
		sa(a);
	}
	else if (first > second && first > third && second < third) // 3 1 2
		ra(a);
	else if (first < second && second > third && first < third)	// 1 3 2
	{
		rra(a);
		sa(a);
	}
	else if (first > second && first < third) // 2 1 3
		sa(a);
	else if (first < second && second > third && first > third)	// 2 3 1
		rra(a);
}

static void	sorting_four(t_stack **a, t_stack **b)
{
	int	min_index;

	if (!a || !*a)
		return ;
	min_index = find_min_index(*a);
	if (min_index == 1)
		ra(*a);
	else if (min_index == 2)
	{
		ra(*a);
		ra(*a);
	}
	else if (min_index == 3)
		rra(*a);
	pb(b, a);
	sorting_three(*a);
	pa(a, b);
}

static void	sorting_five(t_stack **a, t_stack **b)
{
	int	min_index;

	if (!a || !*a)
		return ;
	min_index = find_min_index(*a);
	if (min_index == 1)
		ra(*a);
	else if (min_index == 2)
	{
		ra(*a);
		ra(*a);
	}
	else if (min_index == 3)
	{
		rra(*a);
		rra(*a);
	}
	else if (min_index == 4)
		rra(*a);
	pb(b, a);
	sorting_four(a, b);
	pa(a, b);
}

void	sorting(t_stack *a, t_stack *b)
{
	if (ps_lstsize(a) == 2)
		sa(a);
	else if (ps_lstsize(a) == 3)
		sorting_three(a);
	else if (ps_lstsize(a) == 4)
		sorting_four(&a, &b);
	else if (ps_lstsize(a) == 5)
		sorting_five(&a, &b);
	else if (ps_lstsize(a) >= 6)
		sorting_general(a, b);
}