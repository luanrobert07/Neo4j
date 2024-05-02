class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name, result: 0})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, match_id):
        query = "CREATE (:Match {id: $match_id})"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    def add_player_to_match(self, player_name, match_id):
        query = "MATCH (p:Player {name: $player_name}) MATCH (m:Match {id: $match_id}) CREATE (p)-[:PARTICIPATES_IN]->(m)"
        parameters = {"player_name": player_name, "match_id": match_id}
        self.db.execute_query(query, parameters)

    def update_player_result(self, player_name):
        query = """
        MATCH (p:Player {name: $player_name})
        SET p.result = p.result + 1
        """
        parameters = {"player_name": player_name}
        self.db.execute_query(query, parameters)
        
    def update_match(self, match_id, new_match_id):
        query = "MATCH (m:Match {id: $match_id}) SET m.id = $new_match_id"
        parameters = {"match_id": match_id, "new_match_id": new_match_id}
        self.db.execute_query(query, parameters)

    def update_match_result(self, match_id, results):
        query = "MATCH (m:Match {id: $match_id}) SET m.results = $results"
        parameters = {"match_id": match_id, "results": results}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_player_matches(self, player_name):
        query = "MATCH (p:Player {name: $player_name})-[:PARTICIPATES_IN]->(m:Match) RETURN m.id AS match_id"
        parameters = {"player_name": player_name}
        results = self.db.execute_query(query, parameters)
        return [result["match_id"] for result in results]

    def get_match_info(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) RETURN m.id AS match_id, m.results AS results"
        parameters = {"match_id": match_id}
        return self.db.execute_query(query, parameters)

    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.id AS match_id"
        results = self.db.execute_query(query)
        return [result["match_id"] for result in results]

    def delete_player(self, name):
        query = "MATCH (p:Player {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)
