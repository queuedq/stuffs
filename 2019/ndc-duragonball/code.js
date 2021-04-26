function think(hp, mp, you_hp, you_mp, history, old_games) {
  const action = UnsafeThink(hp, mp, you_hp, you_mp, history, old_games)
  if (action === 'attack' || action === 'charge' || action === 'block') {
    return action
  } else {
    return 'attack'
  }
}

function UnsafeThink(hp, mp, you_hp, you_mp, history, old_games) {
  if (old_games.length === 0) { return 'attack' }

  const opponentStrat = getOpponentStrat(getGameStats(old_games))

  switch (opponentStrat.strat) {
    case 'attack': {
      if (opponentStrat.total === 0) {
        return 'attack'
      }
      if (Math.random() < opponentStrat.attack / opponentStrat.total - 0.15) {
        return 'block'
      }
      return 'attack'
    }

    case 'block': {
      if (mp < 3) {
        if (Math.random() >= 0.5) {
          return 'charge'
        }
      }
      return 'attack'
    }

    default: {
      return 'attack'
    }
  }
}

function getOpponentStrat(gameStats) {
  const totalTurns = gameStats.attack + gameStats.charge + gameStats.block
  if (totalTurns === 0) { return { strat: 'nothing', max: 0, total: 0 } }

  let mostAction = 'attack'
  let maxActionNumber = gameStats.attack
  if (gameStats.charge > maxActionNumber) {
    mostAction = 'charge'
    maxActionNumber = gameStats.charge
  }
  if (gameStats.block > maxActionNumber) {
    mostAction = 'block'
    maxActionNumber = gameStats.block
  }

  if (maxActionNumber >= totalTurns / 2) {
    return { strat: mostAction, max: maxActionNumber, total: totalTurns }
  } else {
    return { strat: 'random', max: maxActionNumber, total: totalTurns }
  }
}

function getGameStats(gameHistory) {
  return gameHistory.reduce(
    function (stats, action) {
      return Object.assign(stats, { action: stats[action] + 1 })
    },
    { 'attack': 0, 'charge': 0, 'block': 0 }
  )
}
