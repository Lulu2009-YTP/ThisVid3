# ThisVid3 Discord Bot Configuration
# Last Updated: 2025-03-21 05:46:24 UTC
# Author: Lulu2009-YTP

import os
from pathlib import Path

# Bot Basic Configuration
BOT_PREFIX = '!'
BOT_STATUS = "Processing Videos 🎥"

# Directory Configuration
BASE_DIR = Path(__file__).parent
DOWNLOAD_DIR = os.path.join(BASE_DIR, 'downloads')
PROCESSED_DIR = os.path.join(BASE_DIR, 'processed')
TEMP_DIR = os.path.join(BASE_DIR, 'temp')
CACHE_DIR = os.path.join(BASE_DIR, 'cache')

# Ensure directories exist
for directory in [DOWNLOAD_DIR, PROCESSED_DIR, TEMP_DIR, CACHE_DIR]:
    os.makedirs(directory, exist_ok=True)

# Video Quality Settings
VIDEO_QUALITY = {
    'default': '720p',
    'available_qualities': ['360p', '480p', '720p', '1080p'],
    'max_file_size': 8 * 1024 * 1024,  # 8MB (Discord file limit)
    'fps': 30,
    'codec': 'libx264',
    'audio_codec': 'aac',
    'audio_bitrate': '192k',
    'compression_settings': {
        'low': {'video_bitrate': '1000k', 'audio_bitrate': '128k'},
        'medium': {'video_bitrate': '2000k', 'audio_bitrate': '192k'},
        'high': {'video_bitrate': '4000k', 'audio_bitrate': '256k'}
    }
}

# Watermark Settings
WATERMARK = {
    'text': 'ThisVid3',
    'font': 'Arial',
    'font_size': 30,
    'color': 'white',
    'opacity': 0.8,
    'position': {
        'location': 'bottom-right',  # Options: top-left, top-right, bottom-left, bottom-right, center
        'padding_x': 20,
        'padding_y': 20
    },
    'animation': {
        'enabled': True,
        'effect': 'fade',  # Options: fade, slide, pulse
        'duration': 2.0
    }
}

# TTS (Text-to-Speech) Settings
TTS = {
    'enabled': True,
    'voice': {
        'gender': 'male',
        'language': 'en',
        'accent': 'com',  # Options: com, co.uk, ca, com.au
        'speed': 1.0,  # 1.0 is normal speed, range: 0.5-2.0
        'pitch': 1.0   # 1.0 is normal pitch, range: 0.5-2.0
    },
    'outro_text': "download now a remix thisvid3",
    'volume': 1.0,
    'fade_duration': 1.0
}

# Remix Parameters
REMIX = {
    'clip_settings': {
        'min_duration': 1.0,  # seconds
        'max_duration': 5.0,  # seconds
        'transition_duration': 0.5,
        'min_clips': 4,
        'max_clips': 8
    },
    'effects': {
        'transitions': ['fade', 'slide', 'dissolve', 'wipe'],
        'video_effects': ['reverse', 'speed_up', 'slow_down', 'mirror'],
        'audio_effects': ['fade', 'reverse', 'pitch_shift'],
        'effect_probability': 0.5  # Probability of applying an effect to each clip
    },
    'synchronization': {
        'enabled': True,
        'beat_detection': True,
        'tempo_range': {
            'min': 80,
            'max': 160
        },
        'sync_points': ['beat', 'bar', 'phrase']
    }
}

# ThisVid2 Feature Integration
THISVID2_FEATURES = {
    'enabled': True,
    'api_endpoint': 'http://localhost:8000/thisvid2/',
    'sync_method': 'auto',  # Options: auto, manual, hybrid
    'compatibility_mode': True,
    'feature_flags': {
        'use_legacy_effects': False,
        'enable_advanced_sync': True,
        'use_beta_features': False
    }
}

# Output Settings
OUTPUT = {
    'format': 'mp4',
    'naming_pattern': '{timestamp}_{effect}_{id}',
    'timestamp_format': '%Y%m%d_%H%M%S',
    'metadata': {
        'include_processing_info': True,
        'include_source_info': True,
        'add_watermark_info': True
    },
    'organization': {
        'create_date_folders': True,
        'categorize_by_type': True,
        'max_files_per_folder': 100
    }
}

# Performance Settings
PERFORMANCE = {
    'max_concurrent_processes': 2,
    'max_memory_usage': '2G',
    'temp_file_cleanup': True,
    'cache_duration': 24 * 60 * 60,  # 24 hours in seconds
    'optimization_level': 'balanced'  # Options: speed, balanced, quality
}

# Error Handling
ERROR_HANDLING = {
    'max_retries': 3,
    'retry_delay': 5,  # seconds
    'log_errors': True,
    'error_notification_channel': None,  # Discord channel ID for error notifications
    'save_failed_jobs': True,
    'failed_jobs_dir': os.path.join(BASE_DIR, 'failed_jobs')
}

# Debug Settings
DEBUG = {
    'enabled': False,
    'verbose_logging': False,
    'save_intermediate_files': False,
    'profile_performance': False,
    'debug_channel': None  # Discord channel ID for debug messages
}

# Resource Management
RESOURCE_LIMITS = {
    'max_video_length': 300,  # seconds
    'max_queue_size': 10,
    'max_storage_size': 10 * 1024 * 1024 * 1024,  # 10GB
    'cleanup_threshold': 0.9,  # 90% of max storage
    'max_processing_time': 300  # seconds
}