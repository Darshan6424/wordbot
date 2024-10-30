import os
from pathlib import Path
import traceback
async def load_cogs(bot):
    # Use Path for better path handling
    cogs_dir = Path('./cogs')
    
    if not cogs_dir.exists():
        print(f"Error: {cogs_dir.absolute()} directory not found!")
        return
        
    # Count successes and failures
    loaded = 0
    failed = 0
    
    print("\nLoading cogs...")
    
    for filepath in cogs_dir.rglob('*.py'):
        # Skip __init__.py and other special files
        if filepath.name.startswith('__'):
            continue
            
        # Convert path to module notation
        relative_path = filepath.relative_to(Path('.'))
        extension = str(relative_path).replace('\\', '.').replace('/', '.')[:-3]
        
        try:
            await bot.load_extension(extension)
            print(f'✓ Loaded: {extension}')
            loaded += 1
            
        except Exception as e:
            print(f'✗ Failed to load {extension}: {str(e)}')
            print(f'Detailed error: {traceback.format_exc()}')
            failed += 1
    
    print(f"\nLoading Summary:")
    print(f"Successfully loaded: {loaded}")
    print(f"Failed to load: {failed}")
    print(f"Total cogs found: {loaded + failed}")
