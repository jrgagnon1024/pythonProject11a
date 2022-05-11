const canvas = document.querySelector('canvas')
const canvasContext = canvas.getContext('2d')

const scoreText = document.querySelector('#scoreText')
let score = 0

canvas.width = innerWidth
canvas.height = innerHeight

class Pacman
{
    static speed = 1

    constructor({position, velocity})
    {
        this.position = position
        this.velocity = velocity
        this.radius = 8
    }

    draw()
    {
        canvasContext.beginPath()
        canvasContext.arc(this.position.x, this.position.y, this.radius, 0, Math.PI * 2)
        canvasContext.fillStyle = 'yellow'
        canvasContext.fill()
        canvasContext.closePath()
    }

    update()
    {
        this.draw()
        velocityCollisionUpdate({player: pacman, xvelocity: pacman.velocity.x, yvelocity: pacman.velocity.y})
        pelletCollision()
        powerPelletCollision()
        ghostCollision()
        this.position.x += this.velocity.x
        this.position.y += this.velocity.y
    }
}

class Ghost
{
    static speed = 1

    constructor({position, velocity, color})
    {
        this.position = position
        this.velocity = velocity
        this.color = color
        this.radius = 8
        this.scared = false
    }

    draw()
    {
        canvasContext.beginPath()
        canvasContext.arc(this.position.x, this.position.y, this.radius, 0, Math.PI * 2)
        canvasContext.fillStyle = this.scared ? 'blue' : this.color
        canvasContext.fill()
        canvasContext.closePath()
    }

    update()
    {
        this.draw()
        velocityCollisionUpdate({player: pacman, xvelocity: pacman.velocity.x, yvelocity: pacman.velocity.y})
        this.position.x += this.velocity.x
        this.position.y += this.velocity.y
    }
}

class Pellet
{
    static points = 10

    constructor({position})
    {
        this.position = position
        this.radius = 2
    }

    draw()
    {
        canvasContext.beginPath()
        canvasContext.arc(this.position.x, this.position.y, this.radius, 0, Math.PI * 2)
        canvasContext.fillStyle = 'yellow'
        canvasContext.fill()
        canvasContext.closePath()
    }
}

class PowerPellet
{
    constructor({position})
    {
        this.position = position
        this.radius = 4
    }

    draw()
    {
        canvasContext.beginPath()
        canvasContext.arc(this.position.x, this.position.y, this.radius, 0, Math.PI * 2)
        canvasContext.fillStyle = 'yellow'
        canvasContext.fill()
        canvasContext.closePath()
    }
}


class Wall
{
    static width = 24
    static height = 24

    constructor({position})
    {
        this.position = position
        //this.image = image
    }

    draw()
    {
        canvasContext.fillStyle = 'blue'
        canvasContext.fillRect(this.position.x, this.position.y, Wall.width, Wall.height)
        //canvasContext.drawImage(this.image, this.position.x, this.position.y)
    }
}

const pacman = new Pacman({position: {x: Wall.width + Wall.width/2, y: Wall.height + Wall.height/2}, velocity: {x: 0, y: 0}})

pacman.draw()

addEventListener('keydown', ({key}) => {
    switch(key){
        case 'w':
            pacman.velocity.x = 0
            pacman.velocity.y = -Pacman.speed
            break
        case 'a':
            pacman.velocity.x = -Pacman.speed
            pacman.velocity.y = 0
            break
        case 's':
            pacman.velocity.x = 0
            pacman.velocity.y = Pacman.speed
            break
        case 'd':
            pacman.velocity.x = Pacman.speed
            pacman.velocity.y = 0
            break
    }
})

const walls = []
const pellets = []
const powerPellets = []
const ghosts = [new Ghost({position: {x: Wall.width * 13 + Wall.width/2, y: Wall.height * 11 + Wall.height/2}, velocity: {x: 0, y: 0}, color: "red"})]

const grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,1,3,3,1,0,1,3,3,3,1,0,1,1,0,1,3,3,3,1,0,1,3,3,1,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
    [1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1],
    [3,3,3,3,3,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,3,3,3,3,3],
    [3,3,3,3,3,1,0,1,1,0,0,0,2,0,0,0,0,0,0,1,1,0,1,3,3,3,3,3],
    [3,3,3,3,3,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,3,3,3,3,3],
    [1,1,1,1,1,1,0,1,1,0,1,3,3,3,3,3,3,1,0,1,1,0,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,1,3,3,3,3,3,3,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,1,1,0,1,3,3,3,3,3,3,1,0,1,1,0,1,1,1,1,1,1],
    [3,3,3,3,3,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,3,3,3,3,3],
    [3,3,3,3,3,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,3,3,3,3,3],
    [3,3,3,3,3,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,3,3,3,3,3],
    [1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
    [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
    [1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]    
]

grid.forEach((row, i, j) => {
    row.forEach((value, j) => {
        if(value === 1){
            walls.push(new Wall({position: {x: Wall.width * j, y: Wall.height * i}}))
        }
        if(value === 0){
            pellets.push( new Pellet({position: {x: Wall.width * j + Wall.width/2, y: Wall.height * i + Wall.height/2}}))
        }
        if(value === 2){
            powerPellets.push( new PowerPellet({position: {x: Wall.width * j + Wall.width/2, y: Wall.height * i + Wall.height/2}}))
        }
    })
})

function wallCollision({player, wall}){
    return(player.position.y - player.radius + player.velocity.y <= wall.position.y + Wall.height && player.position.y + player.radius + player.velocity.y >= wall.position.y && player.position.x - player.radius + player.velocity.x <= wall.position.x + Wall.width && player.position.x + player.radius + player.velocity.x >= wall.position.x)
}

function pelletCollision()
{
    for(let i = pellets.length - 1; 0 <= i; i--)
    {
        const pellet = pellets[i]
        if(Math.hypot(pellet.position.x - pacman.position.x, pellet.position.y - pacman.position.y) < pellet.radius + pacman.radius)
        {
            pellets.splice(i, 1)
            score += 10
            scoreText.innerHTML = score
        }
    }
}

function powerPelletCollision()
{
    for(let i = powerPellets.length - 1; 0 <= i; i--)
    {
        const powerPellet = powerPellets[i]
        if(Math.hypot(powerPellet.position.x - pacman.position.x, powerPellet.position.y - pacman.position.y) < powerPellet.radius + pacman.radius)
        {
            powerPellets.splice(i, 1)

            ghosts.forEach(ghost => {
                ghost.scared = true
                setTimeout(() => {ghost.scared = false}, 5000)
            })
        }
    }
}

function ghostCollision()
{
    for(let i = ghosts.length - 1; 0 <= i; i--)
    {
        const ghost = ghosts[i]
        if(Math.hypot(ghost.position.x - pacman.position.x, ghost.position.y - pacman.position.y) < ghost.radius + pacman.radius)
        {
            if(ghost.scared)
            {
                ghosts.splice(i, 1)
            }
            else
            {
                cancelAnimationFrame(ID)
            }
        }
    }
}

function velocityCollisionUpdate({player, xvelocity, yvelocity}){

    for(let i = 0; i < walls.length; i++){
        const wall = walls[i]
        if(wallCollision({player: {...player, velocity:{x: xvelocity, y: yvelocity}}, wall: wall}))
        {
            player.velocity.x = 0
            player.velocity.y = 0
            return
        }
        else
        {
            player.velocity.x = xvelocity
            player.velocity.y = yvelocity
        }
    }
}

let ID

function animate(){
    ID = requestAnimationFrame(animate)
    canvasContext.clearRect(0, 0, canvas.width, canvas.height)
    walls.forEach((wall) => {
        wall.draw()
    })
    pellets.forEach((pellet, i) => {
        pellet.draw()
    })
    powerPellets.forEach((powerPellet, i) => {
        powerPellet.draw()
    })
    ghosts.forEach((ghost) => {
        ghost.draw()
    })
    pacman.update()
}

function createImage(src)
{
    const image = new Image()
    image.src = src
    return image
}

animate()

if(pellets.length == 0) 
{
    cancelAnimationFrame(ID)
}