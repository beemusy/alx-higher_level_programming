/*
 * File: 13-is_palindrome.c
 * Auth: Blessings Moyo
 */

#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if elements in a
 * linked list are a palindrome
 *
 * @listint_t: linked list
 * @head: pointer to header of linked list
 * Return: 0 if its not a palindrome or 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	if(*head == NULL || (*head)->next == NULL)
		return (1);
	return (0);
	/*finding the middle of the list*/
}
