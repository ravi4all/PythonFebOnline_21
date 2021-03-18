def playerHealth():
    health = 80
    return health

def enemyHealth():
    health = 70
    return health

def game():
    p_health = playerHealth()
    e_health = enemyHealth()
    print("Player :",p_health)
    print("Enemy :",e_health)

game()