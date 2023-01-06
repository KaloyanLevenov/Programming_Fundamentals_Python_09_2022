def valid_length(ticket):
    if len(ticket) == 20:
        return True
    print("invalid ticket")
    return False


def winning_ticket(ticket):
    if valid_length(ticket):
        half_length = int(len(ticket) / 2)
        first_half = ticket[0:half_length + 1]
        second_half = ticket[half_length::]
        for winning_symbol in valid_symbols:
            multi_symbol = winning_symbol * 6
            if multi_symbol in first_half and multi_symbol in second_half:
                return winning_symbol
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        return False


def jackpot(ticket):
    if winning_ticket(ticket):
        half_length = int(len(ticket) / 2)
        first_half = ticket[0:half_length + 1]
        second_half = ticket[half_length::]
        for symbol in valid_symbols:
            multi_symbol = symbol * 10
            if multi_symbol in first_half and multi_symbol in second_half:
                print(f'ticket "{ticket}" - {10}{symbol} Jackpot!')
                break
        else:
            print(f'ticket "{ticket}" - {6}{winning_ticket(ticket)}')
    return False


valid_symbols = ['@', '#', '$', '^']
tickets = input().split(', ')

for ticket in tickets:
    ticket = ticket.strip()
    ticket= ticket.replace(",","")
    jackpot(ticket)
