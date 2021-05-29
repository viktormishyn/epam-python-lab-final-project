import s from "./Game.module.css";

export default function Post({ post }) {
  return (
    <div>
      {/* post */}
      <div className={s.post}>
        {/* post header */}
        <p className={s.post__header}>
          <span>{post.author.username} </span>
          <span>
            <i>[{post.author.email}]</i>
          </span>
          <p className={s.post__header__time}>
            <i>{post.created_at}</i>
            {post.edited ? (
              <span>
                <i>Edited</i>
              </span>
            ) : null}
          </p>
        </p>

        {/* post content */}
        <p>{post.content}</p>

        {/* replies */}
      </div>
    </div>
  );
}
