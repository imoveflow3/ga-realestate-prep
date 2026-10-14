/* The front door's 3D study machine.
 *
 * Source for docs/assets/hero3d.js. Edit this file, then rebuild the bundle:
 *     cd online/hero3d && npm install && npm run build
 * The bundle is committed, so building the site itself still needs nothing
 * but Python.
 *
 * Adapted from the Agentic Factory 3D component (procedural three.js, no
 * models, no images): the same plate, belt and five stations, re-dressed as
 * the path a student takes -- study plan, lessons, practice, mock exam, pass --
 * and re-coloured to the site's green and brass. The page's own panels,
 * modes and camera bar are gone; home.js draws a row of step buttons instead
 * and drives the camera through the handle mount() returns.
 */
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'
import { RoundedBoxGeometry } from 'three/examples/jsm/geometries/RoundedBoxGeometry.js'
import { mergeGeometries } from 'three/examples/jsm/utils/BufferGeometryUtils.js'
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js'

/* In flow order: the index here is the step a student is on. */
export const STEPS = [
  { id: 'plan', name: 'Study plan', desc: 'Two questions, then a plan paced to your test date.' },
  { id: 'lessons', name: 'Lessons', desc: 'Every topic on the exam blueprint, one lesson at a time.' },
  { id: 'practice', name: 'Practice', desc: 'Quizzes that keep coming back to what you miss.' },
  { id: 'mock', name: 'Mock exam', desc: 'Full length, the national and state parts scored separately.' },
  { id: 'pass', name: 'Pass', desc: 'Clear both parts. Then the licence.' },
]

/* The state named on the plate, the mock exam screen, the score report and
   the plan card. It starts at Georgia and works through all fifty. */
const STATES = [
  'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
  'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
  'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
  'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
  'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',
  'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
  'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
  'Washington', 'West Virginia', 'Wisconsin', 'Wyoming',
]
const STATE_SECONDS = 2.4

/* WebGL is the one thing a phone can be missing; ask before loading anything. */
export function supported() {
  try {
    const c = document.createElement('canvas')
    return !!(c.getContext('webgl2') || c.getContext('webgl'))
  } catch (e) {
    return false
  }
}

/**
 * Build the scene inside `host` (an element sized by CSS).
 * opts.onStep(i)  the travelling card reached step i (0-4)
 * opts.onFocus(i) a station was clicked or tapped; -1 means back to overview
 * opts.onReady()  the first frame is on screen
 * opts.frameRight() true while the page's words cover the left of the frame
 * opts.interactive() true while the page cannot scroll, so the scene may take
 *                 the wheel and touch; the handle's setInteractive(on) updates it
 * Returns { focus(i), overview(), dispose() }, or null when WebGL fails.
 */
export function mount(host, opts = {}) {
  const cleanups = []
  const listen = (target, type, fn, o) => {
    target.addEventListener(type, fn, o)
    cleanups.push(() => target.removeEventListener(type, fn, o))
  }
  const dispose = () => {
    for (const fn of cleanups.reverse()) fn()
    cleanups.length = 0
  }
  const frameWidth = () => host.clientWidth
  const frameHeight = () => host.clientHeight
  const fontFamily = getComputedStyle(host).fontFamily || 'system-ui, sans-serif'

  const TAU = Math.PI * 2
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches
  const coarse = matchMedia('(pointer: coarse)').matches
  const BRASS = 0xc9a566,
    GREEN = 0xe6c27a // the pass station: a brighter gold
  const scene = new THREE.Scene()
  const camera = new THREE.PerspectiveCamera(33, (frameWidth() || 1) / (frameHeight() || 1), 0.1, 150)
  let renderer
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' })
  } catch (e) {
    return null
  }
  renderer.setClearColor(0x000000, 0)
  renderer.setPixelRatio(Math.min(devicePixelRatio, frameWidth() < 700 ? 1.5 : 1.75))
  renderer.setSize(frameWidth() || 1, frameHeight() || 1)
  renderer.outputColorSpace = THREE.SRGBColorSpace
  renderer.toneMapping = THREE.ACESFilmicToneMapping
  renderer.toneMappingExposure = 1.12
  renderer.shadowMap.enabled = true
  renderer.shadowMap.type = THREE.PCFShadowMap
  host.appendChild(renderer.domElement)

  const controls = new OrbitControls(camera, renderer.domElement)
  controls.enableDamping = true
  controls.dampingFactor = 0.065
  controls.enablePan = false
  controls.minPolarAngle = 0.09
  controls.maxPolarAngle = Math.PI * 0.475
  controls.rotateSpeed = 0.48
  controls.zoomSpeed = 0.7
  // Hands-on when the page cannot scroll: the wheel or a pinch zooms, a drag or
  // a finger turns the machine. When the page does scroll, the wheel and a
  // finger belong to the page and the scene only takes clicks and taps.
  function setInteractive(on) {
    controls.enableZoom = on
    controls.enableRotate = on || !coarse
    renderer.domElement.style.touchAction = on ? 'none' : 'pan-y'
  }
  setInteractive(opts.interactive ? opts.interactive() : false)

  const pmrem = new THREE.PMREMGenerator(renderer),
    room = new RoomEnvironment()
  const env = pmrem.fromScene(room, 0.04)
  scene.environment = env.texture
  scene.environmentIntensity = 0.62
  room.dispose()
  pmrem.dispose()
  scene.add(new THREE.HemisphereLight(0xf4ecdc, 0x29211a, 2))
  const key = new THREE.DirectionalLight(0xfff1d8, 4.2)
  key.position.set(-4, 12, 7)
  key.castShadow = true
  key.shadow.mapSize.set(2048, 2048)
  Object.assign(key.shadow.camera, { left: -10, right: 10, top: 9, bottom: -9, near: 0.5, far: 35 })
  key.shadow.normalBias = 0.035
  key.shadow.bias = -0.0002
  key.shadow.radius = 4
  scene.add(key)
  const rim = new THREE.DirectionalLight(0xeadcc4, 3.1)
  rim.position.set(3, 7, -8)
  scene.add(rim)
  const warm = new THREE.PointLight(0xffd58a, 24, 20, 2)
  warm.position.set(-4, 5, 3)
  scene.add(warm)
  const front = new THREE.DirectionalLight(0xffffff, 1)
  front.position.set(5, 3, 10)
  scene.add(front)

  const mat = (color, metalness = 0.1, roughness = 0.4, extra = {}) =>
    new THREE.MeshStandardMaterial({ color, metalness, roughness, ...extra })
  const M = {
    body: mat(0x3a342c, 0.75, 0.29),
    base: mat(0x2f2a24, 0.85, 0.32),
    edge: mat(0x8a8172, 0.85, 0.24),
    chrome: mat(0xd6ccb9, 0.92, 0.18),
    dark: mat(0x1a1612, 0.45, 0.38),
    rubber: mat(0x110e0b, 0.1, 0.6),
    amber: mat(BRASS, 0.55, 0.28),
    ivory: mat(0xe0ded4, 0.48, 0.26),
    copper: mat(0xb08a4e, 0.85, 0.3),
    light: mat(BRASS, 0.2, 0.25, { emissive: 0xd9a84e, emissiveIntensity: 1.4 }),
    pass: mat(GREEN, 0.35, 0.3, { emissive: 0xd9a84e, emissiveIntensity: 0.9 }),
    green: mat(0xf0d9a0, 0.1, 0.3, { emissive: 0xd9a84e, emissiveIntensity: 0.7 }),
  }
  const geometries = new Map()
  function boxGeo(w, h, d, r = 0.04) {
    const k = `b${w},${h},${d},${r}`
    if (!geometries.has(k))
      geometries.set(
        k,
        r ? new RoundedBoxGeometry(w, h, d, 2, Math.min(r, w / 3, h / 3, d / 3)) : new THREE.BoxGeometry(w, h, d)
      )
    return geometries.get(k)
  }
  function box(parent, w, h, d, x, y, z, m = M.body, r = 0.04) {
    const o = new THREE.Mesh(boxGeo(w, h, d, r), m)
    o.position.set(x, y, z)
    o.castShadow = true
    o.receiveShadow = true
    parent.add(o)
    return o
  }
  function cyl(parent, r, h, x, y, z, m = M.chrome, r2 = r, segments = 24) {
    const k = `c${r},${r2},${h},${segments}`
    if (!geometries.has(k)) geometries.set(k, new THREE.CylinderGeometry(r, r2, h, segments))
    const o = new THREE.Mesh(geometries.get(k), m)
    o.position.set(x, y, z)
    o.castShadow = true
    o.receiveShadow = true
    parent.add(o)
    return o
  }
  function ball(parent, r, x, y, z, m = M.chrome) {
    const k = `s${r}`
    if (!geometries.has(k)) geometries.set(k, new THREE.SphereGeometry(r, 12, 8))
    const o = new THREE.Mesh(geometries.get(k), m)
    o.position.set(x, y, z)
    parent.add(o)
    return o
  }
  function tube(parent, pts, r, m = M.chrome) {
    const curve = new THREE.CatmullRomCurve3(pts.map((p) => new THREE.Vector3(...p)))
    const o = new THREE.Mesh(new THREE.TubeGeometry(curve, Math.max(12, pts.length * 7), r, 8, false), m)
    o.castShadow = true
    parent.add(o)
    return o
  }
  function screw(parent, x, y, z) {
    cyl(parent, 0.055, 0.026, x, y, z, M.chrome, undefined, 12)
    box(parent, 0.068, 0.005, 0.009, x, y + 0.014, z, M.dark, 0)
  }
  function canvasTexture(w, h, draw) {
    const c = document.createElement('canvas')
    c.width = w
    c.height = h
    const ctx = c.getContext('2d')
    draw(ctx, w, h)
    const t = new THREE.CanvasTexture(c)
    t.colorSpace = THREE.SRGBColorSpace
    t.anisotropy = Math.min(4, renderer.capabilities.getMaxAnisotropy())
    return { texture: t, canvas: c, ctx }
  }
  function print(ctx, txt, x, y, size = 20, color = '#f4f1ea', weight = 500) {
    ctx.fillStyle = color
    ctx.font = `${weight} ${size}px ${fontFamily}`
    ctx.fillText(txt, x, y)
  }
  // Same as print, but shrinks the type until the text fits `maxW` pixels.
  function printFit(ctx, txt, x, y, maxW, size = 20, color = '#f4f1ea', weight = 500) {
    let s = size
    ctx.font = `${weight} ${s}px ${fontFamily}`
    while (s > 8 && ctx.measureText(txt).width > maxW) {
      s -= 1
      ctx.font = `${weight} ${s}px ${fontFamily}`
    }
    print(ctx, txt, x, y, s, color, weight)
    return ctx.measureText(txt).width
  }
  let stateIndex = STATES.indexOf('Georgia')
  const stateName = () => STATES[stateIndex]
  // Canvases that carry the state's name, redrawn each time it changes.
  const stateCanvases = []
  function stateTexture(w, h, draw) {
    const tex = canvasTexture(w, h, draw)
    stateCanvases.push(() => {
      draw(tex.ctx, w, h)
      tex.texture.needsUpdate = true
    })
    return tex
  }
  function screen(parent, w, h, x, y, z, tex) {
    const map = tex.texture || tex
    const o = new THREE.Mesh(new THREE.PlaneGeometry(w, h), new THREE.MeshBasicMaterial({ map, toneMapped: false }))
    o.position.set(x, y, z)
    parent.add(o)
    return o
  }
  // Canvas colours: the site's brass and green on the machine's dark glass.
  const C = {
    brass: '#c9a566',
    brassDeep: '#8a6516',
    green: '#d4ac5a',
    greenDeep: '#7a5a14',
    ink: '#18222c',
    paper: '#f4f1ea',
    glass: '#1d1913',
  }

  const machine = new THREE.Group()
  scene.add(machine)
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(70, 70), new THREE.ShadowMaterial({ opacity: 0.2 }))
  floor.rotation.x = -Math.PI / 2
  floor.position.y = -0.43
  floor.receiveShadow = true
  scene.add(floor)
  const shadow = canvasTexture(128, 128, (c, w, h) => {
    const g = c.createRadialGradient(64, 64, 12, 64, 64, 64)
    g.addColorStop(0, 'rgba(0,0,0,.7)')
    g.addColorStop(0.55, 'rgba(0,0,0,.38)')
    g.addColorStop(1, 'rgba(0,0,0,0)')
    c.fillStyle = g
    c.fillRect(0, 0, w, h)
  })
  const contact = new THREE.Mesh(
    new THREE.PlaneGeometry(18, 13),
    new THREE.MeshBasicMaterial({ map: shadow.texture, transparent: true, depthWrite: false, opacity: 0.55 })
  )
  contact.rotation.x = -Math.PI / 2
  contact.position.y = -0.415
  scene.add(contact)

  // The plate, with the exam's shape engraved along the front edge.
  box(machine, 12.8, 0.38, 8.25, 0, -0.09, 0, M.base, 0.17)
  box(machine, 12.6, 0.055, 8.08, 0, 0.13, 0, M.edge, 0.11)
  box(machine, 12.49, 0.09, 7.96, 0, 0.19, 0, M.body, 0.1)
  box(machine, 12.55, 0.027, 8.02, 0, -0.19, 0, M.dark, 0.06)
  box(machine, 11.9, 0.026, 0.032, 0, -0.17, 4.115, M.light, 0.01)
  for (const x of [-5.6, 5.6])
    for (const z of [-3.35, 3.35]) {
      cyl(machine, 0.39, 0.25, x, -0.31, z, M.rubber)
      cyl(machine, 0.29, 0.09, x, -0.4, z, M.dark)
      screw(machine, x, 0.253, z)
    }
  for (const x of [-6.02, 6.02]) for (const z of [-3.73, 3.73]) screw(machine, x, 0.255, z)
  const engraving = stateTexture(1536, 176, (c, w, h) => {
    c.fillStyle = '#2e2a24'
    c.fillRect(0, 0, w, h)
    c.strokeStyle = '#5a5246'
    c.lineWidth = 2
    c.strokeRect(2, 2, w - 4, h - 4)
    const nameW = printFit(c, stateName().toUpperCase(), 45, 79, 430, 40, '#d9d8cd', 650)
    print(c, '·  salesperson exam  ·  study to pass', 45 + nameW + 30, 79, 34, '#cfc6b6', 450)
    print(c, 'NATIONAL PART    /    STATE PART    /    SCORED SEPARATELY', 47, 133, 19, '#8a8072', 500)
    print(c, 'No. 001', 1360, 130, 23, C.brass)
  })
  const plate = screen(machine, 7.35, 0.84, -0.4, 0.25, 3.51, engraving)
  plate.rotation.x = -Math.PI / 2
  for (let i = 0; i < 16; i++)
    box(machine, 0.015, 0.009, 0.11 + (i % 4) * 0.035, -5.6 + i * 0.09, 0.249, 3.5, M.edge, 0)

  // Stations sit where the original's did; `step` is their place in the student's path.
  const definitions = [
    { step: 1, pos: [-4.15, 0.29, -0.65] }, // lessons (the original's engine)
    { step: 2, pos: [-1.65, 0.29, -2.03] }, // practice
    { step: 3, pos: [1.5, 0.29, -2.08] }, // mock exam
    { step: 0, pos: [4.03, 0.29, 0.12] }, // study plan
    { step: 4, pos: [0.93, 0.29, 1.85] }, // pass
  ]
  const stations = []
  const gears = []
  function gear(parent, x, y, z, r = 0.3) {
    const g = new THREE.Group()
    g.position.set(x, y, z)
    parent.add(g)
    cyl(g, r, 0.09, 0, 0, 0, M.copper)
    cyl(g, r * 0.66, 0.105, 0, 0, 0, M.dark)
    cyl(g, r * 0.22, 0.14, 0, 0, 0, M.chrome)
    for (let i = 0; i < 12; i++) {
      const a = (i / 12) * TAU,
        b = box(g, r * 0.26, 0.085, r * 0.2, Math.cos(a) * r, 0, Math.sin(a) * r, M.copper, 0.008)
      b.rotation.y = -a
    }
    g.userData.moving = true
    gears.push(g)
    return g
  }
  definitions.forEach((d) => {
    const info = STEPS[d.step]
    const group = new THREE.Group()
    group.position.fromArray(d.pos)
    machine.add(group)
    const glowMat = (d.step === 4 ? M.pass : M.light).clone()
    glowMat.emissiveIntensity = 0.5
    box(group, 2.05, 0.12, 1.78, 0, 0.03, 0, M.dark, 0.1)
    box(group, 1.97, 0.03, 1.7, 0, 0.12, 0, glowMat, 0.09)
    box(group, 2.03, 0.17, 1.75, 0, 0.215, 0, M.body, 0.1)
    for (const x of [-0.85, 0.85]) for (const z of [-0.7, 0.7]) screw(group, x, 0.311, z)
    gear(group, -0.35, 0.45, 0, 0.27)
    gear(group, 0.22, 0.45, 0.12, 0.21)
    box(group, 0.6, 0.15, 0.36, 0.52, 0.47, -0.33, M.dark)
    for (let j = 0; j < 6; j++) box(group, 0.025, 0.16, 0.37, 0.3 + j * 0.08, 0.47, -0.33, M.edge, 0.004)
    tube(
      group,
      [
        [-0.7, 0.4, -0.4],
        [-0.55, 0.48, 0.4],
        [0.35, 0.45, 0.6],
        [0.7, 0.58, 0.23],
      ],
      0.023,
      d.step === 4 ? M.pass : M.light
    )
    const plaque = canvasTexture(512, 116, (c, w, h) => {
      c.fillStyle = '#1d1914'
      c.fillRect(0, 0, w, h)
      print(c, String(d.step + 1).padStart(2, '0'), 24, 76, 42, d.step === 4 ? C.green : C.brass, 550)
      print(c, info.name.toUpperCase(), 111, 73, 35, '#e6dfd2', 550)
    })
    screen(group, 1.54, 0.345, 0, 0.27, 0.891, plaque)
    stations.push({ ...info, step: d.step, group, base: new THREE.Vector3(...d.pos), glowMat })
  })
  const byStep = (i) => stations.find((s) => s.step === i)

  // 02 Lessons: a press that prints lesson cards, with two film reels of notes.
  const lessons = byStep(1).group
  box(lessons, 1.74, 0.62, 1.33, 0, 0.65, -0.05, M.ivory, 0.13)
  box(lessons, 1.5, 0.1, 1.16, 0, 0.99, -0.04, M.body, 0.025)
  for (const x of [-0.68, 0.68]) {
    cyl(lessons, 0.065, 1.73, x, 1.35, -0.18, M.chrome)
    box(lessons, 0.22, 1.8, 0.22, x, 1.37, -0.44, M.ivory, 0.035)
  }
  box(lessons, 1.82, 0.27, 0.4, 0, 2.28, -0.35, M.amber, 0.045)
  box(lessons, 1.55, 0.06, 0.06, 0, 2.13, -0.115, M.chrome, 0.01)
  const printhead = new THREE.Group()
  lessons.add(printhead)
  printhead.position.set(0, 1.9, -0.08)
  printhead.userData.moving = true
  box(printhead, 0.45, 0.36, 0.44, 0, 0, 0, M.body, 0.05)
  cyl(printhead, 0.11, 0.13, 0, -0.24, 0.03, M.chrome, 0.04)
  box(printhead, 0.24, 0.045, 0.022, 0, 0.09, 0.23, M.light, 0.01)
  tube(
    lessons,
    [
      [-0.68, 2.1, -0.35],
      [-0.42, 2.52, -0.4],
      [0.25, 2.5, -0.4],
      [0.35, 2.01, -0.12],
    ],
    0.032,
    M.dark
  )
  const reels = []
  for (const [x, y] of [
    [-1.03, 1.82],
    [-0.94, 2.78],
  ]) {
    const reel = new THREE.Group()
    reel.position.set(x, y, -0.48)
    lessons.add(reel)
    reel.userData.moving = true
    const core = cyl(reel, 0.4, 0.22, 0, 0, 0, M.dark)
    core.rotation.x = Math.PI / 2
    for (const z of [-0.14, 0.14]) {
      const disc = cyl(reel, 0.46, 0.045, 0, 0, z, M.chrome)
      disc.rotation.x = Math.PI / 2
      for (let j = 0; j < 6; j++) {
        const a = (j / 6) * TAU
        const hole = cyl(reel, 0.1, 0.006, Math.cos(a) * 0.29, Math.sin(a) * 0.29, z + (z > 0 ? 0.026 : -0.026), M.dark, undefined, 14)
        hole.rotation.x = Math.PI / 2
      }
    }
    const axle = cyl(reel, 0.095, 0.37, 0, 0, 0, M.amber)
    axle.rotation.x = Math.PI / 2
    reels.push(reel)
  }
  tube(
    lessons,
    [
      [-1.36, 2.66, -0.48],
      [-1.5, 2.34, -0.48],
      [-1.34, 1.92, -0.48],
    ],
    0.045,
    M.dark
  )
  const lessonTex = canvasTexture(384, 640, () => {})
  function drawLesson(t) {
    const c = lessonTex.ctx,
      w = 384,
      h = 640
    c.fillStyle = C.brass
    c.fillRect(0, 0, w, h)
    c.fillStyle = '#b8904c'
    c.beginPath()
    c.arc(330, 205, 210, 0, TAU)
    c.fill()
    // An open book, gently turning a page.
    c.strokeStyle = '#1d1914'
    c.lineWidth = 12
    c.lineJoin = 'round'
    const lift = Math.sin(t * 0.9) * 26
    c.beginPath()
    c.moveTo(192, 330)
    c.quadraticCurveTo(130, 290, 70, 312)
    c.lineTo(70, 202)
    c.quadraticCurveTo(130, 180, 192, 222)
    c.quadraticCurveTo(254, 180, 314, 202)
    c.lineTo(314, 312)
    c.quadraticCurveTo(254, 290, 192, 330)
    c.closePath()
    c.stroke()
    c.beginPath()
    c.moveTo(192, 222)
    c.lineTo(192, 330)
    c.stroke()
    c.lineWidth = 7
    c.beginPath()
    c.moveTo(192, 226)
    c.quadraticCurveTo(232, 196 - lift, 290 - lift * 0.6, 214 - lift * 0.5)
    c.stroke()
    print(c, 'LESSON 04', 28, 57, 24, '#242320', 650)
    print(c, 'AGENCY.', 24, 103, 42, '#242320', 700)
    c.fillStyle = '#1d1914'
    c.beginPath()
    c.roundRect(25, 465, 334, 123, 12)
    c.fill()
    const texts = ['Read the lesson.', 'Quiz yourself on it.', 'See what you missed.', 'Then do it again.']
    const n = Math.floor(t * 0.7) % 4
    print(c, texts[n], 45, 505, 25, C.paper, 550)
    print(c, texts[(n + 1) % 4], 45, 547, 25, C.paper, 550)
    c.fillStyle = '#fff7d4'
    c.fillRect(27, 615, Math.max(10, ((t * 0.13) % 1) * 330), 5)
    lessonTex.texture.needsUpdate = true
  }
  drawLesson(0)
  const lessonCard = new THREE.Group()
  lessonCard.userData.moving = true
  lessons.add(lessonCard)
  box(lessonCard, 0.62, 1.08, 0.055, 0, 1.36, 0.61, M.dark, 0.035)
  screen(lessonCard, 0.56, 0.98, 0, 1.36, 0.641, lessonTex)
  box(lessons, 1.14, 0.12, 0.2, 0, 0.83, 0.66, M.dark, 0.025)
  for (const x of [-0.42, 0.42]) {
    const r = cyl(lessons, 0.115, 0.18, x, 0.92, 0.6, M.chrome)
    r.rotation.z = Math.PI / 2
  }
  for (let i = 0; i < 5; i++) box(lessons, 0.08, 0.03, 0.22, -0.38 + i * 0.19, 1.011, -0.02, M.edge, 0.005)

  // 03 Practice: a console running the quiz queue.
  const practice = byStep(2).group
  box(practice, 1.9, 0.66, 1.36, 0, 0.67, -0.04, M.body, 0.11)
  const consoleTop = new THREE.Group()
  consoleTop.position.set(0, 1.01, -0.08)
  consoleTop.rotation.x = -0.32
  practice.add(consoleTop)
  box(consoleTop, 1.76, 0.12, 1.27, 0, 0, 0, M.ivory, 0.04)
  const queue = canvasTexture(640, 340, () => {})
  function drawQueue(t) {
    const c = queue.ctx
    c.fillStyle = C.glass
    c.fillRect(0, 0, 640, 340)
    print(c, 'PRACTICE QUIZ', 25, 45, 21, '#bfb39c', 550)
    print(c, '12 / 20', 510, 45, 20, C.brass, 500)
    const rows = [
      ['Agency', 'IN PROGRESS'],
      ['Contracts', 'NEXT'],
      ['License law', 'REVIEW'],
    ]
    for (let i = 0; i < 3; i++) {
      const y = 74 + i * 76
      c.fillStyle = '#2c261d'
      c.beginPath()
      c.roundRect(21, y, 598, 61, 6)
      c.fill()
      c.fillStyle = i === 0 ? C.brass : '#6b6152'
      c.fillRect(34, y + 10, 27, 41)
      print(c, rows[i][0], 77, y + 29, 19, '#e4dccb')
      print(c, rows[i][1], 77, y + 49, 11, i === 0 ? C.brass : '#a89c86')
      c.fillStyle = '#3d362b'
      c.fillRect(377, y + 26, 214, 7)
      c.fillStyle = i === 0 ? C.green : '#6b6152'
      c.fillRect(377, y + 26, i === 0 ? ((t * 0.15) % 1) * 214 : 41 + i * 27, 7)
    }
    queue.texture.needsUpdate = true
  }
  drawQueue(0)
  const qs = screen(consoleTop, 1.53, 0.79, 0, 0.067, -0.17, queue)
  qs.rotation.x = -Math.PI / 2
  // Four toggles for A, B, C, D.
  const toggles = []
  for (let i = 0; i < 4; i++) {
    const x = -0.57 + i * 0.38
    cyl(consoleTop, 0.074, 0.035, x, 0.1, 0.45, M.dark)
    const t = cyl(consoleTop, 0.025, 0.15, x, 0.19, 0.45, M.chrome)
    t.rotation.x = -0.4
    t.userData.moving = true
    toggles.push(t)
    ball(consoleTop, 0.04, x, 0.275, 0.421, M.ivory)
  }
  cyl(practice, 0.075, 0.06, 0.77, 1.05, -0.62, M.green)
  for (let i = 0; i < 7; i++) box(practice, 0.55, 0.027, 0.02, 0, 0.46 + i * 0.05, 0.655, M.dark, 0.003)

  // 04 Mock exam: a big screen with the two scores side by side.
  const mock = byStep(3).group
  box(mock, 1.35, 0.18, 0.88, 0, 0.44, 0, M.ivory, 0.045)
  cyl(mock, 0.095, 1.04, 0, 0.93, -0.31, M.chrome)
  box(mock, 0.56, 0.91, 0.14, 0, 0.99, -0.34, M.body, 0.04)
  box(mock, 2.42, 1.72, 0.2, 0, 1.94, -0.17, M.ivory, 0.08)
  box(mock, 2.28, 1.59, 0.1, 0, 1.94, -0.044, M.dark, 0.045)
  const examTex = stateTexture(896, 592, (c, w, h) => {
    c.fillStyle = '#f7f2e8'
    c.fillRect(0, 0, w, h)
    c.fillStyle = '#ebe3d3'
    c.fillRect(0, 0, w, 56)
    c.fillStyle = '#c4b9a4'
    for (let i = 0; i < 3; i++) {
      c.beginPath()
      c.arc(26 + i * 19, 27, 4, 0, TAU)
      c.fill()
    }
    print(c, 'MOCK EXAM', 33, 100, 22, C.ink, 650)
    print(c, 'Practice result', 690, 98, 14, '#7a7062')
    // Two score panels: the exam is passed only when both clear the pass mark.
    const parts = [
      ['NATIONAL', '91%', 0.91],
      [stateName().toUpperCase(), '94%', 0.94],
    ]
    parts.forEach(([label, pct, f], i) => {
      const x = 32 + i * 300
      c.fillStyle = i ? '#f6eedc' : '#f6efdd'
      c.beginPath()
      c.roundRect(x, 131, 280, 250, 10)
      c.fill()
      printFit(c, label, x + 22, 172, 236, 18, i ? C.greenDeep : C.brassDeep, 650)
      print(c, pct, x + 20, 270, 84, C.ink, 650)
      c.fillStyle = '#e0d7c6'
      c.fillRect(x + 22, 318, 236, 10)
      c.fillStyle = i ? C.greenDeep : C.brassDeep
      c.fillRect(x + 22, 318, 236 * f, 10)
      c.fillStyle = C.ink
      c.fillRect(x + 22 + 236 * 0.72, 310, 2, 26)
      print(c, 'Pass mark', x + 22, 360, 14, '#7a7062')
    })
    print(c, 'Scored', 652, 197, 36, C.ink, 600)
    print(c, 'twice.', 652, 243, 36, C.ink, 600)
    print(c, 'Each part', 654, 290, 18, '#7e7464')
    print(c, 'on its own.', 654, 316, 18, '#7e7464')
    c.fillStyle = C.greenDeep
    c.beginPath()
    c.roundRect(32, 420, 300, 62, 7)
    c.fill()
    print(c, 'Review answers  ↗', 60, 459, 22, C.paper, 500)
    print(c, 'BUILT TO THE EXAM BLUEPRINT', 33, 560, 12, '#958b7a')
  })
  screen(mock, 2.16, 1.43, 0, 1.95, 0.011, examTex)
  ball(mock, 0.024, 0, 2.747, -0.05, M.dark)
  box(mock, 0.21, 0.019, 0.008, 0, 1.149, 0.013, M.light, 0.003)
  const scoreCard = new THREE.Group()
  scoreCard.userData.moving = true
  mock.add(scoreCard)
  box(scoreCard, 0.59, 0.77, 0.045, 0.94, 0.81, 0.55, M.ivory, 0.025)
  const scoreTex = canvasTexture(220, 290, (c, w, h) => {
    c.fillStyle = C.paper
    c.fillRect(0, 0, w, h)
    c.fillStyle = '#f6eedc'
    c.fillRect(15, 16, 190, 168)
    c.strokeStyle = C.greenDeep
    c.lineWidth = 14
    c.lineCap = 'round'
    c.lineJoin = 'round'
    c.beginPath()
    c.moveTo(70, 100)
    c.lineTo(100, 130)
    c.lineTo(154, 70)
    c.stroke()
    print(c, 'SCORED', 17, 225, 23, '#352f26', 600)
    c.fillStyle = '#c4b9a4'
    c.fillRect(17, 244, 153, 6)
    c.fillRect(17, 258, 104, 5)
  })
  screen(scoreCard, 0.55, 0.72, 0.94, 0.81, 0.575, scoreTex)

  // 01 Study plan: a cabinet that files the days until the test.
  const plan = byStep(0).group
  box(plan, 1.75, 1.77, 1.02, 0, 1.24, -0.13, M.body, 0.12)
  box(plan, 1.58, 0.13, 1.09, 0, 2.16, -0.13, M.amber, 0.04)
  box(plan, 1.47, 1.38, 0.055, 0, 1.31, 0.405, M.dark, 0.025)
  const planTex = canvasTexture(480, 460, (c, w, h) => {
    c.fillStyle = C.glass
    c.fillRect(0, 0, w, h)
    print(c, 'YOUR PLAN', 30, 51, 27, '#efe8da', 550)
    print(c, '21 days to your test', 30, 81, 16, '#a89c86')
    ;[
      ['1', 'Agency', 'Today'],
      ['2', 'Contracts', 'Tomorrow'],
      ['18', 'Mock exam', 'Day 18'],
    ].forEach(([n, topic, when], i) => {
      const y = 110 + i * 100
      c.fillStyle = '#2c261d'
      c.beginPath()
      c.roundRect(22, y, 436, 83, 8)
      c.fill()
      c.fillStyle = [C.brass, '#bdbf9c', C.green][i]
      c.beginPath()
      c.arc(58, y + 40, 21, 0, TAU)
      c.fill()
      c.textAlign = 'center'
      print(c, n, 58, y + 47, 18, '#1a1408', 650)
      c.textAlign = 'left'
      print(c, topic, 93, y + 33, 23, '#efe8da', 550)
      print(c, when, 93, y + 58, 15, '#a89c86')
      print(c, '↗', 410, y + 49, 25, C.brass)
    })
  })
  screen(plan, 1.31, 1.255, 0, 1.37, 0.44, planTex)
  box(plan, 1.27, 0.075, 0.29, 0, 0.57, 0.55, M.chrome, 0.02)
  for (let i = 0; i < 3; i++) box(plan, 1.15, 0.021, 0.12, 0, 0.58 + i * 0.15, -0.35, M.copper, 0.006)
  tube(
    plan,
    [
      [0.69, 0.43, -0.2],
      [0.89, 0.65, -0.2],
      [0.89, 1.8, -0.2],
      [0.65, 1.99, -0.2],
    ],
    0.033,
    M.chrome
  )
  const incoming = new THREE.Group()
  incoming.userData.moving = true
  plan.add(incoming)
  box(incoming, 0.86, 0.42, 0.043, 0, 0, 0, M.light, 0.035)
  const dateTex = canvasTexture(432, 204, (c, w, h) => {
    c.fillStyle = C.brass
    c.fillRect(0, 0, w, h)
    c.fillStyle = '#352f26'
    c.beginPath()
    c.roundRect(28, 56, 62, 76, 8)
    c.fill()
    c.fillStyle = C.brass
    c.fillRect(28, 76, 62, 4)
    c.textAlign = 'center'
    print(c, '21', 59, 118, 28, C.brass, 650)
    c.textAlign = 'left'
    print(c, 'Test date set', 108, 91, 34, '#352f26', 600)
    print(c, 'Plan built  +', 108, 138, 23, '#5b4c22', 500)
  })
  screen(incoming, 0.82, 0.39, 0, 0, 0.026, dateTex)

  // 05 Pass: the score report prints and a green badge drops in.
  const pass = byStep(4).group
  box(pass, 1.91, 0.63, 1.32, 0, 0.65, -0.06, M.ivory, 0.12)
  box(pass, 1.96, 0.19, 1.38, 0, 0.42, -0.04, M.body, 0.04)
  box(pass, 1.37, 0.09, 0.038, 0, 0.44, 0.66, M.dark, 0.01)
  box(pass, 0.37, 0.042, 0.03, 0, 0.45, 0.687, M.chrome, 0.009)
  box(pass, 1.02, 0.25, 0.91, -0.33, 1.04, -0.03, M.body, 0.045)
  for (let row = 0; row < 3; row++)
    for (let col = 0; col < 3; col++)
      box(pass, 0.19, 0.085, 0.17, -0.62 + col * 0.27, 1.21, 0.27 - row * 0.24, col === 2 && row === 2 ? M.pass : M.ivory, 0.022)
  box(pass, 0.64, 0.6, 0.52, 0.58, 1.04, -0.15, M.body, 0.045)
  box(pass, 0.48, 0.07, 0.09, 0.59, 1.37, -0.1, M.dark, 0.01)
  cyl(pass, 0.06, 0.65, -0.35, 1.6, -0.56, M.chrome)
  box(pass, 1.13, 0.46, 0.19, -0.35, 1.98, -0.56, M.body, 0.045)
  const resultTex = canvasTexture(512, 176, (c) => {
    c.fillStyle = '#1e1912'
    c.fillRect(0, 0, 512, 176)
    print(c, 'EXAM RESULT', 22, 44, 23, '#d8c39a', 500)
    print(c, 'PASS', 26, 131, 70, '#f6ead0', 650)
    c.strokeStyle = C.green
    c.lineWidth = 10
    c.lineCap = 'round'
    c.lineJoin = 'round'
    c.beginPath()
    c.moveTo(386, 98)
    c.lineTo(414, 126)
    c.lineTo(466, 66)
    c.stroke()
  })
  screen(pass, 1.015, 0.349, -0.35, 1.98, -0.459, resultTex)
  const report = new THREE.Group()
  report.position.set(0.59, 1.37, -0.1)
  report.userData.moving = true
  pass.add(report)
  const reportTex = stateTexture(280, 540, (c, w, h) => {
    c.fillStyle = C.paper
    c.fillRect(0, 0, w, h)
    c.setLineDash([])
    print(c, 'SCORE REPORT', 25, 52, 24, '#3a342b', 650)
    printFit(c, stateName().toUpperCase(), 25, 87, 230, 19, '#5e5649')
    c.strokeStyle = '#958b7a'
    c.setLineDash([5, 6])
    c.beginPath()
    c.moveTo(22, 115)
    c.lineTo(258, 115)
    c.stroke()
    print(c, 'National', 25, 154, 22, '#3a342b')
    print(c, 'PASS', 190, 154, 20, C.greenDeep, 650)
    printFit(c, stateName(), 25, 190, 155, 22, '#3a342b')
    print(c, 'PASS', 190, 190, 20, C.greenDeep, 650)
    print(c, 'PASSED', 25, 263, 31, C.greenDeep, 650)
    print(c, 'Next: your licence.', 25, 317, 20, '#6e6555')
    for (let i = 0; i < 44; i++) {
      c.fillStyle = '#3a342b'
      c.fillRect(25 + i * 5, 370, 1 + (i % 3), 83)
    }
    print(c, 'No. 0001', 81, 496, 17, '#5e5649')
  })
  const rp = screen(report, 0.41, 0.83, 0, 0.415, 0.01, reportTex)
  rp.material.side = THREE.DoubleSide
  report.rotation.x = -0.16
  const badge = new THREE.Group()
  badge.userData.moving = true
  pass.add(badge)
  const badgeDisc = cyl(badge, 0.22, 0.065, 0, 0, 0, M.pass, undefined, 32)
  badgeDisc.rotation.x = Math.PI / 2
  const badgeRing = new THREE.Mesh(new THREE.TorusGeometry(0.174, 0.014, 6, 32), M.chrome)
  badgeRing.position.z = 0.037
  badge.add(badgeRing)
  const tickTex = canvasTexture(128, 128, (c, w, h) => {
    c.clearRect(0, 0, w, h)
    c.strokeStyle = '#1a1408'
    c.lineWidth = 13
    c.lineCap = 'round'
    c.lineJoin = 'round'
    c.beginPath()
    c.moveTo(36, 66)
    c.lineTo(56, 86)
    c.lineTo(94, 42)
    c.stroke()
  })
  const tick = screen(badge, 0.28, 0.28, 0, 0, 0.04, tickTex)
  tick.material.transparent = true
  cyl(pass, 0.33, 0.09, 1.04, 0.39, 0.55, M.dark)
  cyl(pass, 0.26, 0.025, 1.04, 0.445, 0.55, M.copper)

  // The belt: a closed spline, instanced treads, continuous rails.
  const path = new THREE.CatmullRomCurve3(
    [
      [-3.95, 0.84, 0.65],
      [-3.1, 0.84, -0.12],
      [-1.45, 0.84, -0.79],
      [1.32, 0.84, -0.8],
      [3.3, 0.84, 0.19],
      [3.43, 0.84, 1.21],
      [1.35, 0.84, 2.7],
      [-1.4, 0.84, 2.52],
      [-3.54, 0.84, 1.65],
    ].map((p) => new THREE.Vector3(...p)),
    true,
    'catmullrom',
    0.25
  )
  const belt = new THREE.Group()
  machine.add(belt)
  const frameMesh = new THREE.Mesh(new THREE.TubeGeometry(path, 150, 0.35, 8, true), M.dark)
  frameMesh.scale.y = 0.3
  frameMesh.position.y = 0.51
  belt.add(frameMesh)
  const beltCount = 148,
    beltSlats = new THREE.InstancedMesh(boxGeo(0.135, 0.065, 0.63, 0.012), M.body, beltCount)
  beltSlats.receiveShadow = true
  belt.add(beltSlats)
  beltSlats.instanceMatrix.setUsage(THREE.DynamicDrawUsage)
  const dummy = new THREE.Object3D(),
    pVec = new THREE.Vector3(),
    tVec = new THREE.Vector3()
  function updateBelt(t) {
    for (let i = 0; i < beltCount; i++) {
      const u = (i / beltCount + t * 0.012) % 1
      path.getPointAt(u, pVec)
      path.getTangentAt(u, tVec)
      dummy.position.copy(pVec)
      dummy.rotation.set(0, -Math.atan2(tVec.z, tVec.x), 0)
      dummy.updateMatrix()
      beltSlats.setMatrixAt(i, dummy.matrix)
    }
    beltSlats.instanceMatrix.needsUpdate = true
  }
  updateBelt(0)
  for (const side of [-1, 1]) {
    const pts = []
    for (let i = 0; i <= 160; i++) {
      path.getPointAt(i / 160, pVec)
      path.getTangentAt(i / 160, tVec)
      pts.push(pVec.clone().add(new THREE.Vector3(-tVec.z * 0.36 * side, 0.09, tVec.x * 0.36 * side)))
    }
    belt.add(new THREE.Mesh(new THREE.TubeGeometry(new THREE.CatmullRomCurve3(pts), 160, 0.028, 6, false), M.chrome))
  }
  for (let i = 0; i < 16; i++) {
    const p = path.getPointAt(i / 16)
    cyl(belt, 0.045, 0.43, p.x, 0.53, p.z, M.chrome)
  }
  // Copper lines tie the station footings together, in the original's order.
  for (let i = 0; i < 4; i++) {
    const a = stations[i].base,
      b = stations[i + 1].base
    const curve = new THREE.CatmullRomCurve3([
      a.clone().add(new THREE.Vector3(0.4, 0.12, 0)),
      a.clone().lerp(b, 0.35).add(new THREE.Vector3(0, 0.1, -0.6)),
      a.clone().lerp(b, 0.65).add(new THREE.Vector3(0, 0.1, -0.6)),
      b.clone().add(new THREE.Vector3(-0.4, 0.12, 0)),
    ])
    machine.add(new THREE.Mesh(new THREE.TubeGeometry(curve, 30, 0.054, 8, false), M.copper))
  }

  // The cards that ride the belt change face at each station.
  const notesTex = canvasTexture(256, 352, (c, w, h) => {
    c.fillStyle = '#eeeae0'
    c.fillRect(0, 0, w, h)
    print(c, 'NOTES', 24, 47, 22, '#352f26', 650)
    print(c, '04 / Agency', 24, 85, 15, '#8f8574')
    for (let i = 0; i < 9; i++) {
      c.fillStyle = i === 4 ? C.brass : '#c4b9a4'
      c.fillRect(24, 111 + i * 21, 190 - (i % 3) * 24, 6)
    }
    print(c, 'READ  ✓', 24, 327, 17, C.greenDeep, 600)
  })
  const planCardTex = stateTexture(256, 352, (c) => {
    c.fillStyle = C.brass
    c.fillRect(0, 0, 256, 352)
    print(c, 'YOUR', 21, 48, 24, '#352f26', 650)
    print(c, 'PLAN', 21, 79, 24, '#352f26', 650)
    c.strokeStyle = '#6f5a2a'
    c.lineWidth = 2
    c.strokeRect(23, 112, 210, 139)
    print(c, 'Day 1', 42, 196, 40, '#352f26', 550)
    printFit(c, stateName().toUpperCase() + ' / 01', 23, 320, 210, 17, '#5b4c22')
  })
  const quizTex = canvasTexture(256, 352, (c) => {
    c.fillStyle = C.glass
    c.fillRect(0, 0, 256, 352)
    print(c, 'QUIZ', 21, 48, 24, '#efe8da', 650)
    print(c, 'Q 12 / 20', 21, 78, 16, '#a89c86')
    ;['A', 'B', 'C', 'D'].forEach((l, i) => {
      const y = 106 + i * 56
      c.fillStyle = i === 2 ? C.green : '#2c261d'
      c.beginPath()
      c.roundRect(21, y, 214, 42, 6)
      c.fill()
      print(c, l, 36, y + 28, 18, i === 2 ? '#1a1408' : '#a89c86', 650)
      c.fillStyle = i === 2 ? '#1a1408' : '#6b6152'
      c.fillRect(66, y + 18, 120 - i * 14, 6)
    })
  })
  const faceTextures = [planCardTex, notesTex, quizTex, scoreTex, reportTex]
  const packets = []
  for (let i = 0; i < 6; i++) {
    const g = new THREE.Group()
    g.userData.moving = true
    machine.add(g)
    box(g, 0.47, 0.71, 0.04, 0, 0, 0, M.ivory, 0.022)
    const faces = faceTextures.map((tex) => {
      const s = screen(g, 0.43, 0.665, 0, 0, 0.024, tex)
      s.material.side = THREE.DoubleSide
      s.visible = false
      return s
    })
    packets.push({ group: g, faces, stage: -1, phase: 0 })
  }
  function nearestPort(x, z) {
    let best = 0,
      dist = Infinity
    for (let i = 0; i < 300; i++) {
      const p = path.getPointAt(i / 300),
        d = (p.x - x) ** 2 + (p.z - z) ** 2
      if (d < dist) {
        dist = d
        best = i / 300
      }
    }
    return best
  }
  const practiceU = nearestPort(-1.65, -0.7),
    mockU = nearestPort(1.5, -0.7),
    passU = nearestPort(0.93, 2.65)

  // Merge static geometry per parent and material; moving parts stay separate.
  function compact(group) {
    for (const child of [...group.children]) if (child.isGroup) compact(child)
    const buckets = new Map()
    for (const child of group.children) {
      if (!child.isMesh || child.isInstancedMesh || child.userData.moving || Array.isArray(child.material)) continue
      const k = child.material.uuid
      if (!buckets.has(k)) buckets.set(k, [])
      buckets.get(k).push(child)
    }
    for (const list of buckets.values()) {
      if (list.length < 2) continue
      const geos = list.map((m) => {
        m.updateMatrix()
        const g = m.geometry.index ? m.geometry.toNonIndexed() : m.geometry.clone()
        return g.applyMatrix4(m.matrix)
      })
      const merged = mergeGeometries(geos, false)
      for (const geo of geos) geo.dispose()
      if (!merged) continue
      const mesh = new THREE.Mesh(merged, list[0].material)
      mesh.castShadow = list.some((x) => x.castShadow)
      mesh.receiveShadow = list.some((x) => x.receiveShadow)
      for (const m of list) group.remove(m)
      group.add(mesh)
    }
  }
  compact(machine)
  stations.forEach((s) =>
    s.group.traverse((o) => {
      o.userData.step = s.step
    })
  )
  const pickables = stations.map((s) => s.group)

  // Tooltip, scoped to the host.
  const tooltip = document.createElement('div')
  tooltip.className = 'hero3d-tip'
  tooltip.setAttribute('role', 'tooltip')
  tooltip.innerHTML = '<strong></strong><p></p>'
  host.appendChild(tooltip)
  cleanups.push(() => tooltip.remove())

  // Camera, interaction and the loop.
  let playing = !reduceMotion,
    simTime = 0,
    focused = -1,
    hovered = -1,
    width = frameWidth(),
    height = frameHeight(),
    narrow = width < 560,
    lastInteraction = performance.now(),
    dragging = false,
    wasDragged = false,
    downX = 0,
    downY = 0,
    cameraAnimating = true,
    lastDraw = -1,
    visible = true,
    contextLost = false,
    baseDistance = 25,
    sized = false,
    readySent = false,
    lastStep = -1
  const desiredPosition = new THREE.Vector3(),
    desiredTarget = new THREE.Vector3(0, 1, 0)
  const viewDirection = new THREE.Vector3(10.5, 10.8, 17).normalize()

  function setCameraGoal() {
    if (focused >= 0) {
      desiredTarget.copy(byStep(focused).group.position).add(new THREE.Vector3(0, 1.25, 0))
      desiredPosition.copy(desiredTarget).addScaledVector(viewDirection, baseDistance * 0.48)
    } else {
      // Aim below the plate's centre so the machine rides above the step buttons.
      desiredTarget.set(0, narrow ? 0.45 : 0.55, 0.7)
      desiredPosition.copy(viewDirection).multiplyScalar(baseDistance).add(desiredTarget)
    }
  }
  // Wait for a real size: aspect 0 would put NaN into the camera for good.
  function layoutCamera() {
    if (!frameWidth() || !frameHeight()) return
    const first = !sized
    sized = true
    width = frameWidth()
    height = frameHeight()
    narrow = width < 560
    renderer.setSize(width, height)
    camera.aspect = width / height
    // Behind the page's words, a shifted frustum puts the machine in the right
    // 58% of the frame without moving the orbit target, so it still turns in place.
    const shifted = !!(opts.frameRight && opts.frameRight())
    if (shifted) camera.setViewOffset(width, height, -width * 0.21, 0, width, height)
    else camera.clearViewOffset()
    camera.updateProjectionMatrix()
    const span = 2 * Math.tan(THREE.MathUtils.degToRad(camera.fov / 2))
    // A phone frame is wide and short: leave room for the plate's corners as it turns.
    const share = shifted ? 0.48 : camera.aspect > 1.2 && narrow ? 0.86 : 0.96
    const horizontalFit = 14.4 / (span * camera.aspect * share)
    const verticalFit = 10.4 / (span * (shifted ? 0.8 : 0.92))
    baseDistance = Math.max(horizontalFit, verticalFit)
    controls.minDistance = baseDistance * 0.35
    controls.maxDistance = baseDistance * 1.6
    setCameraGoal()
    cameraAnimating = true
    if (first) {
      camera.position.copy(desiredPosition)
      controls.target.copy(desiredTarget)
      controls.update()
      cameraAnimating = false
    }
  }
  function focus(i) {
    focused = i >= 0 && i < STEPS.length ? i : -1
    lastInteraction = performance.now()
    setCameraGoal()
    cameraAnimating = true
  }
  layoutCamera()
  const resizeObserver = new ResizeObserver(() => layoutCamera())
  resizeObserver.observe(host)
  cleanups.push(() => resizeObserver.disconnect())
  controls.addEventListener('start', () => {
    dragging = true
    cameraAnimating = false
    lastInteraction = performance.now()
  })
  controls.addEventListener('end', () => {
    dragging = false
    lastInteraction = performance.now()
  })

  const raycaster = new THREE.Raycaster(),
    pointer = new THREE.Vector2()
  const local = (e) => {
    const r = host.getBoundingClientRect()
    return [e.clientX - r.left, e.clientY - r.top]
  }
  function hitStation(x, y) {
    pointer.set((x / width) * 2 - 1, (-y / height) * 2 + 1)
    raycaster.setFromCamera(pointer, camera)
    const hits = raycaster.intersectObjects(pickables, true)
    return hits.length ? hits[0].object.userData.step : -1
  }
  const canvas = renderer.domElement
  listen(canvas, 'pointermove', (e) => {
    const [x, y] = local(e)
    if (Math.hypot(x - downX, y - downY) > 5) wasDragged = true
    if (dragging || e.pointerType === 'touch') return
    const step = hitStation(x, y)
    hovered = step
    canvas.style.cursor = step >= 0 ? 'pointer' : coarse ? '' : 'grab'
    tooltip.classList.toggle('on', step >= 0)
    if (step >= 0) {
      const s = STEPS[step]
      tooltip.querySelector('strong').textContent = String(step + 1).padStart(2, '0') + '  ' + s.name
      tooltip.querySelector('p').textContent = s.desc
      tooltip.style.left = Math.min(width - 230, Math.max(8, x + 16)) + 'px'
      tooltip.style.top = Math.max(8, Math.min(height - 90, y - 64)) + 'px'
    }
  })
  listen(canvas, 'pointerleave', () => {
    hovered = -1
    tooltip.classList.remove('on')
  })
  listen(canvas, 'pointerdown', (e) => {
    ;[downX, downY] = local(e)
    wasDragged = false
    tooltip.classList.remove('on')
  })
  listen(canvas, 'pointerup', (e) => {
    if (wasDragged) return
    const [x, y] = local(e)
    const step = hitStation(x, y)
    // A tap on the plate or the background goes back to the whole machine.
    const next = step >= 0 && step !== focused ? step : -1
    if (next === focused) return
    focus(next)
    opts.onFocus && opts.onFocus(next)
  })
  let lastFrame = performance.now()
  listen(document, 'visibilitychange', () => {
    visible = !document.hidden
    lastFrame = performance.now()
  })
  const observer = new IntersectionObserver(
    (entries) => {
      visible = entries[0].isIntersecting && !document.hidden
      lastFrame = performance.now()
    },
    { threshold: 0.01 }
  )
  observer.observe(canvas)
  cleanups.push(() => observer.disconnect())
  listen(canvas, 'webglcontextlost', (e) => {
    e.preventDefault()
    contextLost = true
  })
  listen(canvas, 'webglcontextrestored', () => {
    contextLost = false
    lastFrame = performance.now()
  })

  const scratch = new THREE.Vector3()
  let frameCount = 0,
    measureTime = 0,
    pixelRatio = renderer.getPixelRatio(),
    rafId = 0
  function animate(now) {
    rafId = requestAnimationFrame(animate)
    const dt = Math.max(0, Math.min((now - lastFrame) / 1000, 0.045))
    lastFrame = now
    if (!visible || contextLost) return
    if (playing) simTime += dt
    const nextState = (STATES.indexOf('Georgia') + Math.floor(simTime / STATE_SECONDS)) % STATES.length
    if (nextState !== stateIndex) {
      stateIndex = nextState
      stateCanvases.forEach((redraw) => redraw())
    }
    const t = simTime,
      beat = (t / 4) % 1,
      tact = (t * TAU) / 4,
      smooth = 1 - Math.exp(-dt * 5)
    stations.forEach((s, i) => {
      const pulse = Math.pow(Math.max(0, Math.sin(tact - i * 0.9)), 7)
      const lit = hovered === s.step || focused === s.step || (focused < 0 && lastStep === s.step)
      s.glowMat.emissiveIntensity = THREE.MathUtils.lerp(s.glowMat.emissiveIntensity, lit ? 3.2 : 0.55 + pulse * 0.65, smooth)
    })
    gears.forEach((g, i) => (g.rotation.y = t * (i % 2 ? -1 : 1) * 1.1))
    reels.forEach((r, i) => (r.rotation.z = -t * (i ? 0.65 : 0.85)))
    printhead.position.x = Math.sin(tact) * 0.42
    printhead.position.y = 1.91 + Math.sin(tact * 2) * 0.055
    lessonCard.position.y = beat * 0.25
    scoreCard.position.y = Math.sin(tact) * 0.04
    report.scale.y = 0.2 + Math.min(1, beat * 1.5) * 0.8
    badge.position.set(1.04, 2.7 - Math.min(1, beat * 1.7) ** 2 * 2.17, 0.55)
    badge.rotation.y = t * 3.5
    badge.scale.setScalar(beat > 0.9 ? 1 - (beat - 0.9) * 8 : 1)
    incoming.position.set(Math.sin(beat * Math.PI) * 0.24, 2.9 - beat * 1.9, 1.1 - beat * 0.55)
    incoming.rotation.z = Math.sin(beat * Math.PI) * -0.14
    incoming.scale.setScalar(Math.min(1, beat * 8 + 0.15, (1 - beat) * 7 + 0.1))
    toggles.forEach((o, i) => (o.rotation.x = Math.sin(tact + i) > 0 ? -0.4 : 0.4))
    if (t - lastDraw > 1 / 18 || lastDraw < 0) {
      drawLesson(t)
      drawQueue(t)
      updateBelt(t)
      lastDraw = t
    }
    packets.forEach((packet, i) => {
      const phase = (t / 24 + i / 6) % 1
      packet.phase = phase
      let stage
      if (phase < 0.15) {
        // From the plan cabinet over to the lesson press.
        stage = 0
        const f = phase / 0.15
        packet.group.position.copy(byStep(0).group.position).add(new THREE.Vector3(0, 1.6, 0.6))
        scratch.copy(byStep(1).group.position).add(new THREE.Vector3(0, 1.3, 0.65))
        packet.group.position.lerp(scratch, f)
        packet.group.position.y += Math.sin(f * Math.PI) * 2
        packet.group.rotation.set(0, Math.sin(f * Math.PI) * 0.28, Math.sin(f * Math.PI) * -0.1)
      } else {
        const u = ((phase - 0.15) / 0.85) * passU
        path.getPointAt(u, packet.group.position)
        packet.group.position.y += 0.43
        packet.group.rotation.set(0, 0.18, 0)
        stage = u < practiceU * 0.7 ? 1 : u < mockU * 0.96 ? 2 : u < passU * 0.83 ? 3 : 4
      }
      if (packet.stage !== stage) {
        packet.faces.forEach((f, j) => (f.visible = j === stage))
        packet.stage = stage
      }
      packet.group.scale.setScalar(phase > 0.94 ? Math.max(0.05, (1 - phase) / 0.06) : 1)
    })
    // The first card leads; the step buttons on the page follow it.
    if (packets[0].stage !== lastStep) {
      lastStep = packets[0].stage
      opts.onStep && opts.onStep(lastStep)
    }
    if (focused >= 0 && cameraAnimating) setCameraGoal()
    if (cameraAnimating && !dragging) {
      const speed = 1 - Math.exp(-dt * 3)
      camera.position.lerp(desiredPosition, speed)
      controls.target.lerp(desiredTarget, speed)
      if (camera.position.distanceTo(desiredPosition) < 0.015 && controls.target.distanceTo(desiredTarget) < 0.015)
        cameraAnimating = false
    }
    controls.autoRotate = playing && !dragging && !cameraAnimating && focused < 0 && now - lastInteraction > 5000
    controls.autoRotateSpeed = 0.3
    controls.update(dt)
    renderer.render(scene, camera)
    if (!readySent && sized) {
      readySent = true
      opts.onReady && opts.onReady()
    }
    // Slow device: lower the resolution, never the animation.
    if (playing) {
      frameCount++
      measureTime += dt
      if (measureTime > 4) {
        if (frameCount / measureTime < 43 && pixelRatio > 1) {
          pixelRatio = Math.max(1, pixelRatio - 0.25)
          renderer.setPixelRatio(pixelRatio)
        }
        frameCount = 0
        measureTime = 0
      }
    }
  }
  rafId = requestAnimationFrame(animate)
  cleanups.push(() => {
    cancelAnimationFrame(rafId)
    controls.dispose()
    const textures = new Set()
    scene.traverse((object) => {
      if (object.geometry) object.geometry.dispose()
      const list = object.material ? (Array.isArray(object.material) ? object.material : [object.material]) : []
      for (const material of list) {
        for (const value of Object.values(material)) if (value instanceof THREE.Texture) textures.add(value)
        material.dispose()
      }
    })
    geometries.forEach((g) => g.dispose())
    textures.forEach((t) => t.dispose())
    env.dispose()
    renderer.dispose()
    renderer.forceContextLoss()
    canvas.remove()
  })
  renderer.compile(scene, camera)

  // For checking it in a browser; not part of the page.
  window.__hero3d = {
    getState: () => ({ width, height, narrow, focused, step: lastStep, playing, drawCalls: renderer.info.render.calls }),
  }
  cleanups.push(() => delete window.__hero3d)

  return {
    focus,
    setInteractive,
    overview: () => focus(-1),
    play: () => (playing = true),
    pause: () => (playing = false),
    dispose,
  }
}
