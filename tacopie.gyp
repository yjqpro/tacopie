{
  'targets' : [
    {
      'target_name' : 'tacopie',
      'type' : '<(component)',
      'sources' : [
        '<!@(python <(DEPTH)/build/glob_files.py sources *.cpp)',
        '<!@(python <(DEPTH)/build/glob_files.py includes *.hpp)',
      ],
      'include_dirs': [
        'includes',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'includes',
        ],
      },
    },
  ]
}
