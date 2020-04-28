#include "lists.h"

/**
  * check_cycle - check if linked lists consists a cycle
  * @list: head of linked list
  * Return: 0 if there is no cycle, 1 if there is a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *p = list;
	listint_t *q = list;

	while (p && q && q->next)
	{
		p = p->next;
		q = q->next->next;
		if (q == p)
			return (1);
	}
	return (0);
}
