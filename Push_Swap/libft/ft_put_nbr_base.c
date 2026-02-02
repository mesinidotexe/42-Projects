#include <unistd.h>

void ft_put_nbr_base(long nbr, char *base)
{
    int digits;
    int value;

    digits = 0;
    if (nbr < 0)
    {
        write (1, "-", 1);
        nbr *= -1;
    }
    while (base[digits])
        digits++;
    if (digits < 2)
        return;
    if (nbr >= digits)
        ft_put_nbr_base(nbr / digits, base);
    value = base[nbr % digits];
    write (1, &value, 1);
}

// int	main(void)
// {
// 	/* Base decimal */
// 	write(1, "Decimal:\n", 9);
// 	ft_put_nbr_base(42, "0123456789");
// 	write(1, "\n", 1);
// 	ft_put_nbr_base(-42, "0123456789");
// 	write(1, "\n", 1);
// 	ft_put_nbr_base(0, "0123456789");
// 	write(1, "\n\n", 2);

// 	/* Base binária */
// 	write(1, "Binario:\n", 9);
// 	ft_put_nbr_base(42, "01");
// 	write(1, "\n", 1);
// 	ft_put_nbr_base(-42, "01");
// 	write(1, "\n\n", 2);

// 	/* Base hexadecimal */
// 	write(1, "Hexadecimal:\n", 13);
// 	ft_put_nbr_base(42, "0123456789ABCDEF");
// 	write(1, "\n", 1);
// 	ft_put_nbr_base(-42, "0123456789ABCDEF");
// 	write(1, "\n\n", 2);

// 	/* Base octal */
// 	write(1, "Octal:\n", 7);
// 	ft_put_nbr_base(42, "01234567");
// 	write(1, "\n\n", 2);

// 	/* Base inválida */
// 	write(1, "Base invalida (tamanho 1):\n", 27);
// 	ft_put_nbr_base(42, "0");
// 	write(1, "\n\n", 2);

// 	write(1, "Base vazia:\n", 12);
// 	ft_put_nbr_base(42, "");
// 	write(1, "\n\n", 2);

// 	/* Valores grandes */
// 	write(1, "Valores grandes:\n", 17);
// 	ft_put_nbr_base(2147483647, "0123456789");
// 	write(1, "\n", 1);
// 	ft_put_nbr_base(-2147483648, "0123456789");
// 	write(1, "\n", 1);

// 	return (0);
// }