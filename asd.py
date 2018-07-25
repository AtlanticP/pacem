graph = {}
graph['Jane'] = ['Janet', 'Mike']
graph['Janet'] = ['Jane', 'Gym']
graph['Gym'] = ['Janet', 'Mike', 'Lina']
graph['Mike'] = ['Jane', 'Gym']
graph['Erik'] = ['Mike']
graph['Lina'] = ['Gym', 'Lida']
# graph['Lida'] = ['Vitaliy']
# graph['Vitaliy'] = ['Lida']
graph['Lida'] = []
graph['Vitaliy'] = []

def bfs(person):

  searched_persons = []
  to_search = graph[person]
  
  while to_search:

    person = to_search.pop()

    if person not in searched_persons:
      
      if person == 'Vitaliy':
        return('Yep')
      
      searched_persons.append(person)

      to_search += graph[person]

print(bfs('Jane'))