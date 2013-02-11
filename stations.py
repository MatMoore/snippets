"""
What is the least amount of London tube stations you need so that
the letters in their names cover the entire alphabet?
"""
import string
import array

stations = [
  "Acton Central",
  "Acton Town",
  "Aldgate",
  "Aldgate East",
  "All Saints",
  "Alperton",
  "Amersham",
  "Angel",
  "Archway",
  "Arnos Grove",
  "Arsenal",
  "Baker Street",
  "Balham",
  "Bank",
  "Barbican",
  "Barking",
  "Barkingside",
  "Barons Court",
  "Bayswater",
  "Beckton",
  "Beckton Park",
  "Becontree",
  "Belsize Park",
  "Bermondsey",
  "Bethnal Green",
  "Blackfriars",
  "Blackhorse Road",
  "Blackwall",
  "Bond Street",
  "Borough",
  "Boston Manor",
  "Bounds Green",
  "Bow Church",
  "Bow Road",
  "Brent Cross",
  "Brixton",
  "Bromley-by-Bow",
  "Brondesbury",
  "Brondesbury Park",
  "Buckhurst Hill",
  "Burnt Oak",
  "Caledonian Road",
  "Caledonian Road & Barnsbury",
  "Camden Road",
  "Camden Town",
  "Canada Water",
  "Canary Wharf",
  "Canning Town",
  "Cannon Street",
  "Canonbury",
  "Canons Park",
  "Chalfont & Latimer",
  "Chalk Farm",
  "Chancery Lane",
  "Charing Cross",
  "Chesham",
  "Chigwell",
  "Chiswick Park",
  "Chorleywood",
  "Clapham Common",
  "Clapham North",
  "Clapham South",
  "Cockfosters",
  "Colindale",
  "Colliers Wood",
  "Covent Garden",
  "Crossharbour And London Arena",
  "Croxley",
  "Cutty Sark",
  "Cyprus",
  "Dagenham East",
  "Dagenham Heathway",
  "Dalston Kingsland",
  "Debden",
  "Debtford Bridge",
  "Devons Road",
  "Dollis Hill",
  "Ealing Broadway",
  "Ealing Common",
  "Earls Court",
  "East Acton",
  "East Finchley",
  "East Ham",
  "East India",
  "East Putney",
  "Eastcote",
  "Edgware",
  "Edgware Road",
  "Elephant And Castle",
  "Elm Park",
  "Elverson Road",
  "Embankment",
  "Epping",
  "Euston",
  "Euston Square",
  "Fairlop",
  "Farringdon",
  "Finchley",
  "Finchley Road",
  "Finchley Road And Frognal",
  "Finsbury Park",
  "Fulham Broadway",
  "Gallions Reach",
  "Gants Hill",
  "Gloucester Road",
  "Golders Green",
  "Goldhawk Road",
  "Goodge Street",
  "Gospel Oak",
  "Grange Hill",
  "Great Portland Street",
  "Green Park",
  "Greenford",
  "Greenwich",
  "Gunnersbury",
  "Hackney Central",
  "Hackney Wick",
  "Hainault",
  "Hammersmith",
  "Hampstead Heath",
  "Hampstead",
  "Hanger Lane",
  "Harlesden",
  "Harrow And Wealdstone",
  "Harrow on-the-Hill",
  "Hatton Cross",
  "Heathrow Terminal 4",
  "Heathrow Terminals 1,2,3",
  "Hendon Central",
  "Heron Quays",
  "High Barnet",
  "High Street Kensington",
  "Highbury & Islington",
  "Highgate",
  "Hillingdon",
  "Holborn",
  "Holland Park",
  "Holloway Road",
  "Homerton",
  "Hornchurch",
  "Hounslow Central",
  "Hounslow East",
  "Hounslow West",
  "Hyde Park Corner",
  "Ickenham",
  "Island Gardens",
  "Kennington",
  "Kensal Green",
  "Kensal Rise",
  "Kensington (Olympia)",
  "Kentish Town",
  "Kentish Town West",
  "Kenton",
  "Kew Gardens",
  "Kilburn",
  "Kilburn Park",
  "King's Cross St Pancras?",
  "Kingsbury",
  "Knightsbridge",
  "Ladbroke Grove",
  "Lambeth North?",
  "Lancaster Gate",
  "Latimer Road",
  "Leicester Square",
  "Lewisham",
  "Leyton",
  "Leytonstone",
  "Limehouse",
  "Liverpool Street",
  "London Bridge",
  "Loughton",
  "Manor House",
  "Mansion House",
  "Marble Arch",
  "Marylebone",
  "Maida Vale",
  "Mile End",
  "Mill Hill East",
  "Monument",
  "Moor Park",
  "Moorgate",
  "Morden",
  "Mornington Crescent",
  "Mudchute",
  "Neasden",
  "New Cross Gate",
  "New Cross",
  "Newbury Park",
  "North Acton",
  "North Ealing",
  "North Greenwich",
  "North Harrow",
  "North Wembley",
  "North Woolwich",
  "Northfields",
  "Northolt",
  "Northwick Park",
  "Northwood",
  "Northwood Hills",
  "Notting Hill Gate",
  "Oakwood",
  "Old Street",
  "Osterley",
  "Oval",
  "Oxford Circus",
  "Paddington",
  "Park Royal",
  "Parsons Green",
  "Perivale",
  "Picadilly Circus",
  "Pimlico",
  "Pinner",
  "Plaistow",
  "Poplar",
  "Preston Road",
  "Prince Regent",
  "Pudding Mill Lane",
  "Putney Bridge",
  "Queens Park",
  "Queensbury",
  "Queensway",
  "Ravenscourt Park",
  "Rayners Lane",
  "Redbridge",
  "Regent's Park",
  "Richmond",
  "Rickmansworth",
  "Roding Valley",
  "Rotherhithe",
  "Royal Albert",
  "Royal Oak",
  "Royal Victoria",
  "Ruislip",
  "Ruislip Gardens",
  "Ruislip Manor",
  "Russel Square",
  "Seven Sisters",
  "Shadwell",
  "Shepherd's Bush",
  "Shoreditch",
  "Silvertown",
  "Sloane Square",
  "Snaresbrook",
  "South Acton",
  "South Ealing",
  "South Harrow",
  "South Kensington",
  "South Kenton",
  "South Quay",
  "South Ruislip",
  "South Wimbledon",
  "South Woodford",
  "Southfields",
  "Southgate",
  "Southwark",
  "St. James's Park",
  "St John's Wood",
  "St Paul's",
  "Stamford Brook",
  "Stanmore",
  "Stepney Green",
  "Stockwell",
  "Stonebridge Park",
  "Stratford",
  "Sudbury Hill",
  "Sudbury Town",
  "Surrey Quays",
  "Swiss Cottage",
  "Temple",
  "Theydon Bois",
  "Tooting Bec",
  "Tooting Broadway",
  "Tottenham Court Road",
  "Tottenham Hale",
  "Totteridge And Whetstone",
  "Tower Gateway",
  "Tower Hill",
  "Tufnell Park",
  "Turnham Green",
  "Turnpike Lane",
  "Upminster",
  "Upminster Bridge",
  "Upney",
  "Upton Park",
  "Uxbridge",
  "Vauxhall",
  "Victoria",
  "Walthamstow Central",
  "Wanstead",
  "Wapping",
  "Warren Street",
  "Warwick Avenue",
  "Waterloo",
  "Watford",
  "Wembley Central",
  "Wembley Park",
  "West Acton",
  "West Brompton",
  "West Finchley",
  "West Ham",
  "West Hampstead",
  "West Harrow",
  "West India Quay",
  "West Kensington",
  "West Ruislip",
  "Westbourne Park",
  "Westferry",
  "Westminster",
  "White City",
  "Whitechapel",
  "Willesden Green",
  "Willesden Junction",
  "Wimbledon",
  "Wimbledon Park",
  "Wood Green",
  "Woodford",
  "Woodside Park"
]

def normalise(station):
  "Lowercase everything and filter out non-letters"
  return frozenset((i.lower() for i in station if i in string.letters))

INFINITY = 300  # Sentinel value for an infinite number of stations

A_NUM = ord('a')
class Alphabets(object):
  """Represents all possible subsets of the alphabet contained
  in a list of words.
  There are 2^n subsets, which can each be identified by an integer."""
  def __init__(self, stations):
    self.alphabet = sorted((reduce(lambda a, b: set(a) | set(b), stations)))
    self.size = len(self.alphabet) # size of the full alphabet
    self.combis = 2 ** self.size   # number of combinations
    self.maxint = self.combis - 1

  def _int_to_set(self, n):
    "Iterate over all letters encoded in n"
    for letter in xrange(self.size):
      if (1 << letter) & n:
        yield self.alphabet[letter]

  def int_to_set(self, n):
    "Set of letters encoded in n"
    return frozenset(self._int_to_set(n))

  def set_to_int(self, s):
    "Encode a subset of letters as an integer"
    # TODO
    # THIS ASSUMES ALPHABET IS CONSECUTIVE AND BEGINS WITH A!!!
    return sum((1 << (ord(i)-A_NUM) for i in s))

  def __iter__(self):
    for i in xrange(self.combis):
      yield self.int_to_set(i)

class Solver(object):
  def __init__(self, words):
    words = [normalise(word) for word in words]
    self.words = words
    self.alphabets = Alphabets(words)
    self.results = array.array('B', (0 for i in xrange(self.alphabets.combis)))

  def solve(self):
    """
    Calculate the number of stations in the solution by building up intermediate
    solutions that use smaller alphabets.

    The solution for an alphabet A is 1 station more than the solution
    to A-chars(s), for all stations s.
    """
    # Every subset of letters
    for i, existing in enumerate(self.alphabets):
      existing_count = self.results[i]
      # Every choice of next station
      for station in self.words:
        if station - existing: # each station must contribute new letters
          new = self.alphabets.set_to_int(station | existing)

          if station > existing:
            # The current station provides all letters in the current subset
            new_count = 1
          elif existing_count:
            # Some other words got us the current subset, and now we can extend
            new_count = existing_count + 1
          else:
            # We haven't actually found the "existing" subset, how embarassing!
            continue

          # If we've already got to this new subset with less stations,
          # then this set is useless
          if self.results[new] and self.results[new] < new_count:
            continue

          self.results[new] = new_count

          if new == self.alphabets.maxint:
            # Got em all
            return self.results[new]

  def rebuild(self, last_seen=None):
    """
    Work out the stations in the solution by examining the results array
    """
    last_seen = last_seen or self.alphabets.maxint
    last_result = self.results[last_seen]
    alphabet = self.alphabets.int_to_set(last_seen)
    #print alphabet, last_result, last_seen
    for station in self.words:
      # Take this station as the last step in a valid solution
      # If it is in the optimal solution, then the result excluding
      # this station should be one word less than the optimal result
      # we found.
      new = self.alphabets.set_to_int(alphabet - station)
      new_result = self.results[new]
      #if last_seen == 455:
        #print station, alphabet-station, new_result
      if last_result - new_result == 1:
        yield station
        #print alphabet - station
        #print new
        for other in self.rebuild(new):
          yield other
        return

if __name__ == '__main__':
  stations = [
      'abc',
      'bcd',
      'cde',
      'def',
      'efg',
      'fgh',
      'ghi',
      'hia',
      'iab'
  ]

  solver = Solver(stations)
  print '-' * 80
  print solver.solve()
  print '-' * 80

  for i in solver.rebuild():
    print i
