def problesolve(head,leg):
    for i in range(head+1):
        rabbit=i
        chiken = head -i
        if((rabbit*4)+(2*chiken)==leg ):
            return rabbit,chiken
    return

print(problesolve(35,94))
