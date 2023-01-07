#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/** 
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: linked list
 * Return: 0 if there is a cycle, 1 if there is no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if(list == null)
		return (0);

	while (fast != null && slow != null)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}

	return (0);
}
