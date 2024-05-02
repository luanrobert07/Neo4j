from database import Database
from game_database import GameDatabase

db = Database("bolt://3.94.121.54:7687", "neo4j", "abbreviation-development-tilling")
db.drop_all()

game_db = GameDatabase(db)

# Adicionando 10 jogadores
for i in range(1, 11):
    player_name = f"Player_{i}"
    game_db.create_player(player_name)
    print(f"Jogador {player_name} adicionado com sucesso.")

# Imprimindo os jogadores
print("\nLista de Jogadores:")
print(game_db.get_players())

# Criando duas partidas
game_db.create_match("Partida1")
print("\nPartida 'Partida1' criada com sucesso.")
game_db.create_match("Partida2")
print("Partida 'Partida2' criada com sucesso.")

# Adicionando jogadores na Partida1
for i in range(1, 6):
    player_name = f"Player_{i}"
    game_db.add_player_to_match(player_name, "Partida1")
    print(f"Jogador {player_name} adicionado à Partida1.")

# Adicionando jogadores na Partida2
for i in range(6, 11):
    player_name = f"Player_{i}"
    game_db.add_player_to_match(player_name, "Partida2")
    print(f"Jogador {player_name} adicionado à Partida2.")

# Imprimindo as partidas que cada jogador está participando
for i in range(1, 11):
    player_name = f"Player_{i}"
    print(f"\nPartidas em que {player_name} está participando:")
    print(game_db.get_player_matches(player_name))

# Atualizando o resultado das partidas e quem venceu
game_db.update_match_result("Partida1", "Player_1")
game_db.update_player_result("Player_1")
print("\nResultado da 'Partida1' atualizado. O jogador 'Player_1' venceu.")

game_db.update_match_result("Partida2", "Player_6")
game_db.update_player_result("Player_6")
print("\nResultado da 'Partida2' atualizado. O jogador 'Player_6' venceu.")

# Imprimindo as informações da partida
print("\nInformações da Partida1:")
print(game_db.get_match_info("Partida1"))

print("\nInformações da Partida2:")
print(game_db.get_match_info("Partida2"))

# Deletando um jogador e uma partida
game_db.delete_player("Player_2")
game_db.delete_match("Partida1")
print("\nJogador 'Player_2' deletado. Partida 'Partida1' deletada.")

# Imprimindo os jogadores e partidas restantes
print("\nLista de Jogadores após exclusão:")
print(game_db.get_players())

print("\nLista de Partidas após exclusão:")
print(game_db.get_matches())

db.close()
