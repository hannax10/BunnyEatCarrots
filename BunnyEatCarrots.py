def find_center(M):
  """Get the center(s) of a matrix, if more than one center cell, return the one with the highest value"""
  num_row = len(M)
  num_col = len(M[0])
  
  candidate_row = []
  if num_row % 2 == 0:
    candidate_row = [num_row / 2 - 1, num_row / 2]
  else:
    candidate_row = [num_row / 2]

  candidate_col = []
  if num_col % 2 == 0:
    candidate_col = [num_col / 2 - 1, num_col / 2]
  else:
    candidate_col = [num_col / 2]

  candidate_center = ()
  max_val = 0
  for r in candidate_row:
    for c in candidate_col:
      if M[r][c] > max_val: 
        max_val = M[r][c]
        candidate_center = (r, c)

  return candidate_center


def eat_helper(M, visited, curr, num_carrots):
  # eat the carrots at curr location
  x = curr[0]
  y = curr[1]
  num_row = len(M)
  num_col = len(M[0])
  num_carrots += M[x][y]
  visited[x, y] = 1
  
  # find next-move candidate
  next_list = []
  candidate_next = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
  for c in candidate_next:
    # if out of boundary, skip
    if c[0] >= num_row or c[0] < 0 or c[1] >= num_col or c[1] < 0: continue
    # if vistied or no carrots, skip
    if visited[c[0], c[1]] == 1 or M[c[0]][c[1]] == 0: continue
    next_list.append(c)

  # no more move, just return
  if len(next_list) == 0: return num_carrots
  
  # find final list for the next move, may have >1 candidates
  max_val = max([M[x[0]][x[1]] for x in next_list])
  # get the (x,y) position corresponding to max val
  final_list = []
  for c in next_list:
    if M[c[0]][c[1]] == max_val:
      final_list.append(c)
  
  # traverse all final candidate, and find the max carrots
  max_carrots = max([eat_helper(M, visited, c, num_carrots) for c in final_list])
  visited[x, y] = 0
  return max_carrots

def eat(M):
  num_row = len(M)
  num_col = len(M[0])
  visited = {(i, j) : 0 for i in range(num_row) for j in range(num_row) }

  curr = find_center(M)
  return eat_helper(M, visited, curr, 0)

if __name__ == '__main__':
  M = [[5, 7, 8, 6, 3], [0, 0, 7, 0, 4], [4, 6, 3, 4, 9], [3, 1, 0, 5, 8]]
  assert eat(M) == 27
