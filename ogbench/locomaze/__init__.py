from gymnasium.envs.registration import register

visual_dict = dict(
    ob_type='pixels',
    render_mode='rgb_array',
    width=64,
    height=64,
    camera_name='back',
)

register(
    id='pointmaze-medium-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='point',
        maze_env_type='maze',
        maze_type='medium',
    ),
)
register(
    id='pointmaze-large-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='point',
        maze_env_type='maze',
        maze_type='large',
    ),
)
register(
    id='pointmaze-giant-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='point',
        maze_env_type='maze',
        maze_type='giant',
    ),
)
register(
    id='pointmaze-teleport-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='point',
        maze_env_type='maze',
        maze_type='teleport',
    ),
)

register(
    id='antmaze-medium-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=5000,
    kwargs=dict(
        loco_env_type='ant',
        maze_env_type='maze',
        maze_type='medium',
    ),
)
register(
    id='visual-antmaze-medium-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='ant',
        maze_env_type='maze',
        maze_type='medium',
        **visual_dict,
    ),
)
register(
    id='antmaze-large-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='ant',
        maze_env_type='maze',
        maze_type='large',
    ),
)
register(
    id='visual-antmaze-large-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='ant',
        maze_env_type='maze',
        maze_type='large',
        **visual_dict,
    ),
)
register(
    id='antmaze-giant-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='ant',
        maze_env_type='maze',
        maze_type='giant',
    ),
)
register(
    id='visual-antmaze-giant-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='ant',
        maze_env_type='maze',
        maze_type='giant',
        **visual_dict,
    ),
)
register(
    id='antmaze-teleport-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='ant',
        maze_env_type='maze',
        maze_type='teleport',
    ),
)
register(
    id='visual-antmaze-teleport-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='ant',
        maze_env_type='maze',
        maze_type='teleport',
        **visual_dict,
    ),
)

register(
    id='antsoccer-arena-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='ant',
        maze_env_type='ball',
        maze_type='arena',
    ),
)
register(
    id='antsoccer-medium-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=1000,
    kwargs=dict(
        loco_env_type='ant',
        maze_env_type='ball',
        maze_type='medium',
    ),
)

register(
    id='humanoidmaze-medium-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=2000,
    kwargs=dict(
        loco_env_type='humanoid',
        maze_env_type='maze',
        maze_type='medium',
    ),
)
register(
    id='visual-humanoidmaze-medium-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=2000,
    kwargs=dict(
        loco_env_type='humanoid',
        maze_env_type='maze',
        maze_type='medium',
        **visual_dict,
    ),
)
register(
    id='humanoidmaze-large-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=2000,
    kwargs=dict(
        loco_env_type='humanoid',
        maze_env_type='maze',
        maze_type='large',
    ),
)
register(
    id='visual-humanoidmaze-large-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=2000,
    kwargs=dict(
        loco_env_type='humanoid',
        maze_env_type='maze',
        maze_type='large',
        **visual_dict,
    ),
)
register(
    id='humanoidmaze-giant-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=4000,
    kwargs=dict(
        loco_env_type='humanoid',
        maze_env_type='maze',
        maze_type='giant',
    ),
)
register(
    id='visual-humanoidmaze-giant-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=4000,
    kwargs=dict(
        loco_env_type='humanoid',
        maze_env_type='maze',
        maze_type='giant',
        **visual_dict,
    ),
)
register(
    id='humanoidmaze-teleport-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=2000,
    kwargs=dict(
        loco_env_type='humanoid',
        maze_env_type='maze',
        maze_type='teleport',
    ),
)
register(
    id='visual-humanoidmaze-teleport-v0',
    entry_point='ogbench.locomaze.maze:make_maze_env',
    max_episode_steps=2000,
    kwargs=dict(
        loco_env_type='humanoid',
        maze_env_type='maze',
        maze_type='teleport',
        **visual_dict,
    ),
)
